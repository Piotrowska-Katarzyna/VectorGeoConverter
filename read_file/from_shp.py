import geopandas as gpd

def from_shp(file):
    gdf = gpd.read_file(file)
    return gdf