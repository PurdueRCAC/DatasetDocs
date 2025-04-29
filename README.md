# DatasetDocs

This repository serves two purposes:
1. It hosts a documentation generator for Lmod dataset module files
2. It contains the generated documentation that is hosted on Read the Docs

## Documentation

The documentation for all available datasets can be found online at [ReadTheDocs](https://datasetdocs.readthedocs.io/). This documentation is automatically generated from Lmod module files and provides detailed information about available datasets, their versions, and associated environment variables.

The documentation is stored in the `/docs` directory of this repository and is continuously built and updated on Read the Docs.

### Use of Datasets

The datasets provided in this repository are federated and play a crucial role in enhancing the efficacy of HPC-optimized workflows across various research domains. Anvil's community dataset storage offers smooth and high-speed access to large-scale datasets, significantly benefiting scientific workflows. The hundreds of terabytes of meteorological and geospatial datasets available on Anvil have been essential for the seamless operation of our tools and scientific efforts, allowing researchers to focus more on scientific discovery rather than navigating data-related challenges.

For more information about Anvil and its capabilities, please visit the [RCAC Anvil page](https://www.rcac.purdue.edu/compute/anvil).

## Documentation Generator

The documentation generator tool automatically creates and maintains documentation for scientific datasets by parsing Lmod module files and creating structured documentation in reStructuredText (rst) format.

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
├── index.rst               # Main documentation index
├── category1/              # Top-level dataset category
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

## AI Search Functionality (`ai_search`)

The `ai_search` directory provides advanced AI-powered search and knowledge management tools that integrate with the DatasetDocs ecosystem. These tools enable programmatic uploading, tagging, and management of documentation files as well as conversational search via large language models (LLMs).

### Overview of Modules

- **`knowledge_manager.py`**: Handles API interactions for managing the knowledge base. Supports uploading files, adding files to knowledge bases, tagging documents, retrieving document lists, and deleting documents via RESTful endpoints. This is the core for programmatic knowledge base management.
- **`chat.py`**: Provides a command-line chatbot interface that connects to an LLM API (such as OpenWebUI/AnvilGPT). It allows users to ask questions and receive answers based on the indexed documentation and datasets.
- **`dataset_uploader.py`**: Automates the process of finding, renaming, and uploading `.rst` documentation files into the knowledge base, associating them with the correct knowledge base for datasets.
- **`config.py`**: Loads API keys and endpoint URLs from a `secrets.json` configuration file, enabling secure and flexible deployment.

These tools are designed to:
- Automate ingestion and management of dataset documentation into an AI-powered knowledge base
- Enable conversational and programmatic search over documentation using LLMs
- Support tagging, organization, and bulk management of documentation assets

See the individual module docstrings and code for usage examples and further details.

## Contributing

Contributions are welcome! You can contribute in several ways:
- Improving the documentation generator
- Fixing documentation errors
- Enhancing the documentation structure
- Adding new features

Please feel free to submit a Pull Request.

## License

This project is licensed under the Open Source License License - see the [LICENSE](LICENSE.txt) file for details.