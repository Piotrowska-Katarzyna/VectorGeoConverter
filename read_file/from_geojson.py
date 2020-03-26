import geopandas as gpd

def from_geojson(file):
    gdf = gpd.read_file(file)
    return gdf