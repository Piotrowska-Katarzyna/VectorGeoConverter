import geopandas as gpd

def from_gml(file, csv_geo_columns):
    gdf = gpd.read_file(file)
    return gdf