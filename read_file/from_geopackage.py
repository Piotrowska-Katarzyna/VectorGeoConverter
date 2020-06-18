import geopandas as gpd

def from_geopackage(file, csv_geo_columns):
    gdf = gpd.read_file(file)
    return gdf