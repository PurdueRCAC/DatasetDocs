===========
MERIT_Hydro
===========

Version: 2019-05-28

Category: **geospatial**

Description
-----------

MERIT Hydro (Multi-Error-Removed Improved-Terrain Hydrography)

MERIT Hydro is a high-resolution global hydrography dataset developed to enhance the accuracy of river networks and watershed boundaries. By correcting errors in existing digital elevation models, it provides detailed information on river flow directions, streamlines, and catchment areas. The dataset is utilized in hydrological modeling and water resource management.

This dataset contains data with the following attributes:

* Time Resolution: N/A

* Spatial Resolution: N/A

* DOI: 10.1029/2019WR024873

* Link: https://app.globus.org/file-manager?origin_id=ed0c7900-6369-4340-9354-12be791ee8e4&origin_path=%2F

**Tips:**

* Use echo $ENV_NAME to check the environment value.

* To see all environment variables related to MERIT_HYDRO, you can load the module then use: env | grep MERIT_HYDRO

* To unload the module and remove the environment settings: module unload MERIT_HYDRO

Usage
-----

To find and load available datasets::

    $ module avail
    $ module load datasets
    $ module spider datasets/geospatial/MERIT_Hydro

Environment Variables
-------------------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - **Variable Name**
     - **Value**
   * - ``MERIT_HYDRO_DIR``
     - ``/anvil/datasets/geospatial/MERIT_Hydro/dir``
   * - ``MERIT_HYDRO_ELV``
     - ``/anvil/datasets/geospatial/MERIT_Hydro/elv``
   * - ``MERIT_HYDRO_HND``
     - ``/anvil/datasets/geospatial/MERIT_Hydro/hnd``
   * - ``MERIT_HYDRO_UPA``
     - ``/anvil/datasets/geospatial/MERIT_Hydro/upa``
   * - ``MERIT_HYDRO_UPG``
     - ``/anvil/datasets/geospatial/MERIT_Hydro/upg``
   * - ``MERIT_HYDRO_WTH``
     - ``/anvil/datasets/geospatial/MERIT_Hydro/wth``
   * - ``MERIT_HYDRO_HOME``
     - ``/anvil/datasets/geospatial/MERIT_Hydro``
   * - ``RCAC_MERIT_HYDRO_ROOT``
     - ``/anvil/datasets/geospatial/MERIT_Hydro``
   * - ``RCAC_MERIT_HYDRO_VERSION``
     - ``2019-05-28``
