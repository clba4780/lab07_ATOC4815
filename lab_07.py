import numpy as np
import xarray as xr

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

# Load our CAMulator sample dataset
ds = xr.open_dataset('sample_data_camulator.nc')

coordinates = ds['TREHFHT'].sel(latitude=slice(35,72), longitude=slice(-25,65))

