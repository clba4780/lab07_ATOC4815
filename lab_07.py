import numpy as np
import xarray as xr

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

ds = xr.open_dataset("sample_data_camulator.nc")

print ("Dimensions:", dict(ds.dims))
print ("Coordinates:", list(ds.coords))
print ("Global Attributes", ds.attrs)
print ("TREFHT Attributes", ds['TREFHT'].attrs)

region = ds['TREFHT'].sel(
    latitude=(slice(30,50)), 
    longitude=(slice(240,270))
    )
print (region.shape)