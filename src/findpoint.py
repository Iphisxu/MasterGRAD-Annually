import numpy as np

def findpoint(in_lon, in_lat, ncfile):
    """
    in_lon: longitude of the station
    in_lat: latitude of the station
    ncfile: xarray dataarray that contains coordinates 'longitude' and 'latitude'
    nearest_point: output of the dataarray
    """

    # Compute the distances between each grid point and the specified [lon, lat] location
    distances = ((ncfile.longitude - in_lon)**2 + (ncfile.latitude - in_lat)**2)**0.5

    # Find the minimum distance and corresponding index in the flattened array
    min_distance = distances.min()
    min_index = distances.argmin()

    # Convert the flattened index to 2D index
    y_index, x_index = np.unravel_index(min_index, ncfile[0,0,:,:].shape)

    # Get the value of the DataArray at the nearest grid point
    # nearest_point = ncfile.isel(x=x_index, y=y_index)
    
    return x_index, y_index


'''
# 距离加权算法 from ChatGPT 2024-03-30

from scipy.spatial.distance import cdist
def find_nearest_grid_point(latitude, longitude, grid_latitudes, grid_longitudes):
    # 将经纬度转换为二维数组
    points = np.vstack([latitude, longitude]).T
    
    # 计算所有网格点与指定点的距离
    distances = cdist(points, np.vstack([grid_latitudes, grid_longitudes]).T)
    
    # 找到距离最近的网格点的索引
    nearest_index = np.unravel_index(np.argmin(distances), distances.shape)
    
    # 返回最近的网格点的经纬度
    nearest_latitude = grid_latitudes[nearest_index[1]]
    nearest_longitude = grid_longitudes[nearest_index[0]]
    
    return nearest_latitude, nearest_longitude

def weighted_average_value(latitude, longitude, grid_latitudes, grid_longitudes, grid_values):
    # 找到距离最近的四个网格点的索引
    nearest_indices = np.argsort(cdist(np.vstack([latitude, longitude]).T, np.vstack([grid_latitudes, grid_longitudes]).T))[:, :4]
    
    # 计算距离指定点最近的四个网格点的距离的倒数作为权重
    weights = 1 / cdist(np.vstack([latitude, longitude]).T, np.vstack([grid_latitudes[nearest_indices], grid_longitudes[nearest_indices]]))
    
    # 对值进行加权平均
    weighted_average = np.sum(grid_values[nearest_indices[:, 0]] * weights[:, 0]) / np.sum(weights[:, 0])
    
    return weighted_average

# 示例用法
# 假设有网格数据：各个格点的经纬度和值
grid_latitudes = np.random.uniform(-90, 90, size=(10, 10))
grid_longitudes = np.random.uniform(-180, 180, size=(10, 10))
grid_values = np.random.rand(10, 10)

# 指定一个经纬度点
latitude = 30
longitude = 100

# 找到距离指定点最近的网格点
nearest_latitude, nearest_longitude = find_nearest_grid_point(latitude, longitude, grid_latitudes, grid_longitudes)
print("距离指定点最近的网格点的经纬度:", nearest_latitude, nearest_longitude)

# 计算指定点的加权平均值
weighted_average = weighted_average_value(latitude, longitude, grid_latitudes, grid_longitudes, grid_values)
print("指定点的加权平均值:", weighted_average)
'''