import numpy as np
import xarray as xr

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

# Load our CAMulator sample dataset
ds = xr.open_dataset('sample_data_camulator.nc')
ds_coords = ds.assign_coords(longitude =((ds.longitude+180)%360)-180)

europe = ds_coords['TREFHT'].isel(time=0).sel(latitude=slice(35,72), longitude=slice(-25,45))
print (europe)
fig, ax = plt.subplots(
    figsize = (10,5),
    subplot_kw= {'projection': ccrs.Robinson()})

europe.plot(
    ax = ax,
    transform=ccrs.PlateCarree(),
    cmap='GnBu', 
    cbar_kwargs={'label': 'TREFHT (K)', 
                 'shrink': 0.7, 
                 'orientation': 'horizontal', 
                 'pad': 0.05}
)
# 4. Add coastlines and gridlines
ax.coastlines(linewidth=0.8)
ax.gridlines(draw_labels=True)
plt.show()