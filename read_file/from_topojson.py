import geopandas as gpd

def from_topojson(file, csv_geo_columns):
    gdf = gpd.read_file(file)
    return gdf