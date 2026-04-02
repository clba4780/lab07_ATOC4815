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
print ("PRECT Attributes", ds['PRECT'].attrs)

# Select a region and average over the latitude and longitude - one value per time step
region = ds['PRECT'].sel(
    latitude=(slice(10,30)), 
    longitude=(slice(240,270))
    )
print ("Western-US Region shape: ", region.shape)
print (region)

spatial_mean = region.mean(dim=['latitude','longitude'])
print (f"Shape: {spatial_mean.shape}")
print (spatial_mean.values)

# plot time series
plt.figure()
spatial_mean.plot()
plt.title('Regional Mean Precipitation Over Mexico (PRECT)')
plt.xlabel("Time (days)")
plt.ylabel("Precipitation (mm/s)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('regional_mean_precipitation.png', dpi=150, bbox_inches = 'tight')
print ("regional_mean_precipitation.png saved successfully.")

# compute the anomoly
time_mean = spatial_mean.mean(dim='time')

anomaly = spatial_mean - time_mean

print ("Anomalies (first week):")
print (anomaly.isel(time=slice(0,7)).values)

plt.figure()
anomaly.plot()
plt.title('Regional Precipitation Anomaly over Mexico (relative to time mean)')
plt.xlabel("Time (days)")
plt.ylabel("Precipitation (mm/s)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('precipitation_anomaly.png', dpi=150, bbox_inches = 'tight')
print ("precipitation_anomaly.png saved successfully.")

# make a robinson projection map
fig, ax = plt.subplots(
    figsize = (10,5),
    subplot_kw = {'projection': ccrs.Robinson()},
)

region.isel(time=0).plot(
    ax = ax,
    transform = ccrs.PlateCarree(),
    cmap = 'Blues',
    cbar_kwargs = {'label': 'Precipitation', 'shrink': 0.7}
)

ax.coastlines(linewidth=0.8)
ax.add_feature(cfeature.BORDERS, linewidth = 0.5, alpha = 0.5)
ax.add_feature(cfeature.LAND, linewidth = 0.8, alpha = 0.8)
ax.set_title('PRECT Precipitaton Anomaly Map Over Mexico')
plt.tight_layout()
plt.savefig('regional_anomaly_mapping.png', dpi = 150, bbox_inches = 'tight')
print("regional_anomaly_mapping.png saved successfully.")
