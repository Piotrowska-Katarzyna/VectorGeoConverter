import geopandas as gpd

def from_geopackage(file):
    gdf = gpd.read_file(file)
    return gdf