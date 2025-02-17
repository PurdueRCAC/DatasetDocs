help([[
MERIT Hydro (Multi-Error-Removed Improved-Terrain Hydrography)

MERIT Hydro is a high-resolution global hydrography dataset developed to enhance the accuracy of river networks and
watershed boundaries. By correcting errors in existing digital elevation models, it provides detailed information on
river flow directions, streamlines, and catchment areas. The dataset is utilized in hydrological modeling and water
resource management.

This dataset contains data with the following attributes:
  - Time Resolution: N/A
  - Spatial Resolution: N/A
  - DOI: 10.1029/2019WR024873
  - Link: https://app.globus.org/file-manager?origin_id=ed0c7900-6369-4340-9354-12be791ee8e4&origin_path=%2F

Environment variables included:
-------------------------------------------------------------
$MERIT_HYDRO_DIR      Location: /anvil/datasets/geospatial/MERIT_Hydro/dir
$MERIT_HYDRO_ELV      Location: /anvil/datasets/geospatial/MERIT_Hydro/elv
$MERIT_HYDRO_HND      Location: /anvil/datasets/geospatial/MERIT_Hydro/hnd
$MERIT_HYDRO_UPA      Location: /anvil/datasets/geospatial/MERIT_Hydro/upa
$MERIT_HYDRO_UPG      Location: /anvil/datasets/geospatial/MERIT_Hydro/upg

1 additional environment variables not shown.

$MERIT_HYDRO_HOME     Location: /anvil/datasets/geospatial/MERIT_Hydro
$MERIT_HYDRO_ROOT     Location: /anvil/datasets/geospatial/MERIT_Hydro
$MERIT_HYDRO_VERSION  Version: 2019-05-28

Tips:
- Use echo $ENV_NAME to check the environment value.
- To see all environment variables related to MERIT_HYDRO, you can load the module then use: env | grep MERIT_HYDRO
- To unload the module and remove the environment settings: module unload MERIT_HYDRO
-------------------------------------------------------------
]])

local modroot="/anvil/datasets/geospatial/MERIT_Hydro"

setenv("MERIT_HYDRO_DIR", modroot.."/dir")
setenv("MERIT_HYDRO_ELV", modroot.."/elv")
setenv("MERIT_HYDRO_HND", modroot.."/hnd")
setenv("MERIT_HYDRO_UPA", modroot.."/upa")
setenv("MERIT_HYDRO_UPG", modroot.."/upg")
setenv("MERIT_HYDRO_WTH", modroot.."/wth")

setenv("MERIT_HYDRO_HOME", modroot)
setenv("RCAC_MERIT_HYDRO_ROOT", modroot)
setenv("RCAC_MERIT_HYDRO_VERSION", "2019-05-28")