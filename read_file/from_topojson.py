import geopandas as gpd

def from_topojson(file):
    gdf = gpd.read_file(file)
    return gdf