# DatasetDocs

This repository serves two purposes:
1. It hosts a documentation generator for Lmod dataset module files
2. It contains the generated documentation that is hosted on Read the Docs

## Documentation

The documentation for all available datasets can be found online at [ReadTheDocs](https://datasetdocs.readthedocs.io/). This documentation is automatically generated from Lmod module files and provides detailed information about available datasets, their versions, and associated environment variables.

The documentation is stored in the `/docs` directory of this repository and is continuously built and updated on Read the Docs.

## Documentation Generator

The documentation generator tool automatically creates and maintains documentation for scientific datasets by parsing Lmod module files and creating structured documentation in reStructuredText format.

### Features

- Recursively scans directories containing Lmod (.lua) module files
- Extracts and formats help text from module files
- Captures environment variables set by the modules
- Automatically detects version information from date-based filenames (YYYY-MM-DD format)
- Generates structured documentation in reStructuredText format
- Builds documentation using Sphinx and hosts it on Read the Docs
- Maintains hierarchical documentation structure mirroring the dataset organization

### Installation

1. Clone this repository:
```bash
git clone https://github.com/PurdueRCAC/DatasetDocs.git
cd DatasetDocs
```

2. Install Python dependencies:
```bash
pip install -r docs/requirements.txt
```

### Usage

The main script `generate_docs.py` can be run as follows:

```bash
python generate_docs.py \
  --datasets-dir /path/to/lmod/datasets \
  --output-dir /path/to/DatasetDocs/docs
```

#### Arguments

- `--datasets-dir`: Directory containing the Lmod (.lua) module files
- `--output-dir`: Directory where the generated documentation will be written

### Documentation Structure

The generated documentation follows this structure:

```
docs/
├── index.rst                 # Main documentation index
├── category1/               # Top-level dataset category
│   ├── dataset1/           # Dataset subdirectory
│   │   └── YYYY-MM-DD.rst  # Version-specific documentation
│   └── index.rst           # Category index
└── category2/
    └── ...
```

### Building Documentation Locally

While the documentation is automatically built on Read the Docs, you can also build it locally using Sphinx:

```bash
cd docs
make html
```

The built documentation will be available in `docs/_build/html/`.

## Contributing

Contributions are welcome! You can contribute in several ways:
- Improving the documentation generator
- Fixing documentation errors
- Enhancing the documentation structure
- Adding new features

Please feel free to submit a Pull Request.

## License

[Add your license information here]