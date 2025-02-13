===========================================
Purdue RCAC Dataset Documentation Home
===========================================

Welcome to the Purdue RCAC Dataset Documentation, a ReadTheDocs portal designed to provide researchers with comprehensive information about the datasets hosted on Purdue RCAC’s Anvil. For more details on the hosting environment, please visit the `RCAC Anvil website <https://www.rcac.purdue.edu/anvil>`_.

Introduction
============

This documentation serves as a centralized guide to navigating and utilizing the diverse datasets available through Purdue RCAC. Each dataset module is packaged with a set of environment variables and is managed using Lmod, the module system that enables you to easily load and unload datasets as needed.

If you want to look in specific categories, here are some of the key sections:
- **Category Overview:** Browse datasets grouped by scientific domains or research interests.
- **Dataset Details:** Access in-depth metadata for each dataset, including time and spatial resolution, DOI, and publication date.
- **Usage Instructions:** Learn how to load modules, inspect environment variables, and leverage Lmod's module spider feature.

Dataset Categories
==================
Below are the top-level dataset categories available in this documentation:

.. toctree::
   :maxdepth: 1
   :caption: Categories

   Covariates/index
   geospatial/index
   hydrological/index
   igenomes/index
   meteorological/index

Each category groups datasets by their scientific focus, helping you quickly locate the data most relevant to your research.

Module Spider & Module Loading
===============================

Lmod's ``module spider`` command is a powerful tool that allows you to search for available modules and view detailed information about each one. For instance, to find a dataset module, you can run:

.. code-block:: bash

   module spider <dataset_name>

Once you have identified the module, load it with:

.. code-block:: bash

   module load <dataset_name>

This approach ensures that you can easily integrate datasets into your research environment.

Environment Variable Creation Criteria
========================================

Each dataset module automatically generates a set of environment variables based on the underlying file structure and dataset metadata. The criteria used in the ``generate_lmod.py`` script include:

- **Sanitization:** Environment variable names are sanitized to allow only alphanumeric characters and underscores. Invalid characters are replaced, and names beginning with a digit are prefixed with an underscore.
- **Directory Structure Analysis:** 
  - Parent directories are always included as environment variables.
  - Subdirectories are processed provided the number does not exceed a cutoff (currently set to 25). If a directory exceeds this limit, its children are skipped.
- **Metadata File Handling:**
  - Metadata files (e.g., ``.txt``, ``.json``, ``.yaml``, ``.sh``) are included only if their count is below a defined threshold (currently set to 10).
- **Display Limit:** To maintain clarity, only the first few environment variables (up to 5) are displayed in the module help section, with an indication if additional variables exist.

For a detailed look at how these criteria are implemented, see the `generate_lmod.py script <https://github.com/PurdueRCAC/DatasetDocs/blob/main/scripts/generate_lmod.py>`_.

Additional Resources
====================

- `RCAC Anvil website <https://www.rcac.purdue.edu/anvil>`_
- `DatasetDocs GitHub repository <https://github.com/PurdueRCAC/DatasetDocs>`_
- For a comprehensive guide on using Lmod and environment modules, please refer to the official Lmod documentation.

Contact
=======

For any data requests, questions, or further assistance, please contact:

Jonathan Oppenheimer  
Email: `joppenhe@purdue.edu <mailto:joppenhe@purdue.edu>`_

Thank you for using the Purdue RCAC Dataset Documentation. We hope this resource enhances your research experience by streamlining access to high-quality datasets.