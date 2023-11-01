import numpy as np
import shapely.geometry as sgeom
from shapely.prepared import prep

# silence the warning note
import warnings
warnings.filterwarnings("ignore")

def polygon_to_mask(polygon, x, y):
    '''
    Generate a mask array of points falling into the polygon
    
    Example:
    
    shp = gpd.read_file(shapefile)
    lon = ncfile.longitude
    lat = ncfile.latitude

    mask = polygon_to_mask(shp.geometry[0],lon,lat)
    mask_da = xr.DataArray(mask,dims=('y','x'))

    masked_data = data.where(mask_da)
    data_mean   = masked_data.mean(dim=['y','x'],skipna=True)
    '''
    x = np.atleast_1d(x)
    y = np.atleast_1d(y)
    mask = np.zeros(x.shape, dtype=bool)

    # if each point falls into a polygon, without boundaries
    prepared = prep(polygon)
    for index in np.ndindex(x.shape):
        point = sgeom.Point(x[index], y[index])
        if prepared.contains(point):
            mask[index] = True

    return mask
