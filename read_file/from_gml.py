import geopandas as gpd

def from_gml(file):
    gdf = gpd.read_file(file)
    return gdf