gravity-wave-parameterization
=============================

:doc:`← Back to geoai <../geoai/index>`

.. list-table:: Dataset Metadata
   :header-rows: 1

   * - Field
     - Value
   * - **Folder**
     - ``/datasets/geoai/ibm-nasa-geospatial/gravity-wave-parameterization``
   * - **Discipline**
     - GeoAI / Armospheric Science / Climate Science
   * - **Link**
     - `Access Data <https://huggingface.co/datasets/ibm-nasa-geospatial/gravity-wave-parameterization>`__
   * - **Public**
     - ``True``
   * - **Publication Date**
     - 2024-10-30
   * - **Downloaded**
     - 2025-09-10
   * - **Data Type**
     - NetCDF
   * - **Dataset Size**
     - 39G
   * - **Number of Files**
     - 56
   * - **Usage Policy Link**
     - https://choosealicense.com/licenses/apache-2.0/

Description
-----------
Data format description for the nonlocal gravity wave parameterization dataset<br><br>Data Source<br>The dataset contains input and output training pairs computed using ECMWF's ERA5. The dataset was computed for the years 2010, 2012, 2014, and 2015. One month (from the validation set) is provided here for testing.<br><br>Variables Shape<br>1. Input shape: TIME x IDIM x LAT x LON<br>2. Output shape: TIME x ODIM x LAT x LON<br>Here, IDIM = 491, ODIM = 366, LAT=64, LON=128, TIME index ranges from 0 to 24*31 for months with 31 days

Usage
-----
.. code-block:: bash

   $ module avail
   $ module load datasets
   $ module load geoai/ibm-nasa-geospatial/gravity-wave-parameterization/2024-10-30

Usage Policy
------------
This dataset is released under the Apache License 2.0.
The Apache 2.0 License permits users to use, modify, and distribute the dataset for academic, research, and commercial purposes, provided that proper attribution is given and a copy of the license is included with any redistributed or derivative works. Users are encouraged to acknowledge the IBM–NASA Geospatial team and cite this dataset in publications or applications developed using it.

See also: https://choosealicense.com/licenses/apache-2.0/

Citation
--------
IBM–NASA Geospatial. (2024). Gravity Wave Parameterization Dataset (v1.0) [Dataset]. Hugging Face. https://huggingface.co/datasets/ibm-nasa-geospatial/gravity-wave-parameterization

BibTeX
------
.. code-block:: bibtex

   @dataset{ibm_nasa_gravity_wave_parameterization_2024,
     title = {Gravity Wave Parameterization Dataset (v1.0)},
     author = {IBM–NASA Geospatial},
     year = {2024},
     howpublished = {\url{https://huggingface.co/datasets/ibm-nasa-geospatial/gravity-wave-parameterization}},
     note = {Available on Hugging Face Datasets}
   }
