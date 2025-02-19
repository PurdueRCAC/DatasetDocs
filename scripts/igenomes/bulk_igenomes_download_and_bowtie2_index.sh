#!/bin/bash
#
#SBATCH --job-name=bulk_igenomes_index
#SBATCH --output=bulk_igenomes_index_%j.out
#SBATCH --error=bulk_igenomes_index_%j.err
#SBATCH --time=24:00:00
#SBATCH --account=cda090008
#SBATCH --partition=wholenode
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=64
#SBATCH --mem=128G

set -e

############################################
# 1) Activate conda environment with bowtie2
############################################
eval "$(conda shell.bash hook)"
conda activate bioinformatics

############################################
# 2) Define which species / assemblies / releases to process
#    Format: species:assembly:release
#    IMPORTANT: The species name must match the Ensembl FTP folder exactly (lowercase_with_underscores).
############################################
organisms=(
    # Mammals
    # "mus_musculus:GRCm39:110"               # Mouse
    # "bos_taurus:ARS-UCD1.2:110"             # Cow
    # "canis_lupus_familiaris:CanFam4:110"    # Dog

    # Other vertebrates
    # "danio_rerio:GRCz11:110"                # Zebrafish
    # "oryzias_latipes:ASM223467v1:110"       # Medaka

    # Chicken
    # "gallus_gallus:GRCg7b:110"              # Chicken

    # Plants (on Ensembl Plants)
    "zea_mays:B73RefGen_v5:60"               # Maize (Ensembl Plants)
    "oryza_sativa:IRGSP-1.0:60"              # Rice (Ensembl Plants / RAP-DB)
)

############################################
# 3) Function to download FASTA/GTF + build Bowtie2 index
############################################
download_and_build_index () {
    local SPECIES="$1"   # e.g. oryzias_latipes
    local ASSEMBLY="$2"  # e.g. ASM223467v1
    local RELEASE="$3"   # e.g. 110
    local SOURCE="Ensembl"

    echo "========================================"
    echo "PROCESSING SPECIES: ${SPECIES}, ASSEMBLY: ${ASSEMBLY}, RELEASE: ${RELEASE}"
    echo "========================================"

    #-----------------------------
    # iGenomes-like structure:
    # <Species>/<Source>/<Assembly>/
    #   ├── Annotation/Genes/
    #   └── Sequence/Chromosomes/          # individual chromosome FASTA
    #   └── Sequence/WholeGenomeFasta/     # single concatenated FASTA
    #   └── Sequence/Bowtie2Index/
    #-----------------------------
    local BASE_DIR="${SPECIES}/${SOURCE}/${ASSEMBLY}"
    local CHR_DIR="${BASE_DIR}/Sequence/Chromosomes"
    local WGF_DIR="${BASE_DIR}/Sequence/WholeGenomeFasta"
    local BWT2_DIR="${BASE_DIR}/Sequence/Bowtie2Index"
    local GTF_DIR="${BASE_DIR}/Annotation/Genes"

    mkdir -p "${CHR_DIR}" "${WGF_DIR}" "${BWT2_DIR}" "${GTF_DIR}"

    #-----------------------------
    # Ensembl FTP paths
    #-----------------------------
    if [[ "$SPECIES" == "arabidopsis_thaliana" || \
          "$SPECIES" == "zea_mays" || \
          "$SPECIES" == "oryza_sativa" ]]; then
        # Ensembl Plants subdomain
        ENSEMBL_FTP_BASE="ftp://ftp.ensemblgenomes.org/pub/plants/release-${RELEASE}"
    else
        # Main Ensembl
        ENSEMBL_FTP_BASE="ftp://ftp.ensembl.org/pub/release-${RELEASE}"
    fi

    local ENSEMBL_FTP_FASTA="${ENSEMBL_FTP_BASE}/fasta/${SPECIES}/dna/"
    local ENSEMBL_FTP_GTF="${ENSEMBL_FTP_BASE}/gtf/${SPECIES}/"

    #-----------------------------
    # 3a) Download FASTA into Chromosomes/
    #-----------------------------
    echo "Downloading FASTA from: ${ENSEMBL_FTP_FASTA}"
    wget --recursive \
         --no-parent \
         --no-directories \
         --directory-prefix="${CHR_DIR}" \
         --accept "*.fa.gz" \
         "${ENSEMBL_FTP_FASTA}"

    # Unzip FASTA files in Chromosomes/
    echo "Unzipping FASTA files..."
    for gzfile in "${CHR_DIR}"/*.fa.gz; do
        [ -e "$gzfile" ] && gunzip -fv "$gzfile"
    done

    #-----------------------------
    # 3b) Create WholeGenomeFasta/genome.fa by concatenating all .fa in Chromosomes/
    #-----------------------------
    echo "Creating concatenated genome.fa in WholeGenomeFasta/"
    cat "${CHR_DIR}"/*.fa > "${WGF_DIR}/genome.fa"

    #-----------------------------
    # 3c) Download GTF into Annotation/Genes
    #-----------------------------
    echo "Downloading GTF from: ${ENSEMBL_FTP_GTF}"
    wget --recursive \
         --no-parent \
         --no-directories \
         --directory-prefix="${GTF_DIR}" \
         --accept "*.gtf.gz" \
         "${ENSEMBL_FTP_GTF}"

    # Unzip GTF
    echo "Unzipping GTF files..."
    for gzfile in "${GTF_DIR}"/*.gtf.gz; do
        [ -e "$gzfile" ] && gunzip -fv "$gzfile"
    done

    #-----------------------------
    # 3d) Symlink genome.fa into Bowtie2Index/
    #    so we don't duplicate large files
    #-----------------------------
    echo "Creating symlink to genome.fa in Bowtie2Index..."
    # Remove any existing genome.fa (or symlink) in BWT2_DIR
    rm -f "${BWT2_DIR}/genome.fa"

    # Make a relative symlink so it stays valid if you move the base directory as a unit
    ln -s ../WholeGenomeFasta/genome.fa "${BWT2_DIR}/genome.fa"

    #-----------------------------
    # 3e) Build Bowtie2 index from that symlink
    #-----------------------------
    echo "Building Bowtie2 index for ${SPECIES}..."
    bowtie2-build --threads 8 "${BWT2_DIR}/genome.fa" "${BWT2_DIR}/genome"

    echo "Done building Bowtie2 index for ${SPECIES}"
    echo "Bowtie2 index folder: ${BWT2_DIR}"
    echo
}

############################################
# 4) Iterate over each organism
############################################
for org in "${organisms[@]}"; do
    IFS=":" read -r SPECIES ASSEMBLY RELEASE <<< "$org"

    # Call the function to do the actual work
    download_and_build_index "$SPECIES" "$ASSEMBLY" "$RELEASE"
done

echo "========================================"
echo "ALL DONE!"
echo "========================================"

# If 'tree' is available, show final structure (optional)
command -v tree > /dev/null && tree