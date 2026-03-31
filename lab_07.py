import numpy as np
import xarray as xr

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

ds = xr.open_dataset("sample_data_camulator.nc")

# Explore structure
print ("Dimensions:", dict(ds.dims))
print ("Coordinates:", list(ds.coords))
print ("Global Attributes", ds.attrs)
print ("TREFHT Attributes", ds['TREFHT'].attrs)

# Select a region and average over the latitude and longitude - one value per time step
region = ds['TREFHT'].sel(
    latitude=(slice(30,50)), 
    longitude=(slice(240,270))
    )
print ("Western-US Region shape: ", region.shape)
print (region)

spatial_mean = ds['TREFHT'].mean(dim=['latitude','longitude'])
print (f"Shape: {spatial_mean.shape}")
print (spatial_mean.values)
# plot time series
ds["TREFHT"].isel(time=0).plot(cmap='plasma')
plt.title('Flat lat/lon plot')
plt.tight_layout
plt.show()
# compute the anomoly

# make a robinson projection map
