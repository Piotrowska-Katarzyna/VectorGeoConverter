import numpy as np
import geopandas as gpd
import topojson
from shapely import geometry

def from_topojson(file, type):
    df = pd.read_file(file)
    gdf = gpd.GeoDataFrame(df,coordinateX, coordinateY)
    return gdf
