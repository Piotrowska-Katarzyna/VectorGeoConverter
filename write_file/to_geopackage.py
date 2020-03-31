import geopandas as gpd 

def to_geopackage(gdf, filename, layername):
    gdf.to_file(filename + ".gpkg", layer = layername, driver='GPKG'