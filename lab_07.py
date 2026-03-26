import numpy as np
import xarray as xr

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

# Load our CAMulator sample dataset
ds = xr.open_dataset('sample_data_camulator.nc')


fig, ax = plt.subplots(
    figsize = (10,5),
    subplot_kw= {'projection': ccrs.Robinson()}
)
# 2. Choose a good sequential colormap for precipitation (hint: 'GnBu' or 'Blues')
# 3. Place the colorbar horizontally below the map
ds['TREFHT'].isel(time=0, latitude=slice(35,72), longitude=slice(25,65)).plot(
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