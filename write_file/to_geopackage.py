import geopandas as gpd 

def to_geopackage(gdf, filename):
    gdf.to_file(filename + ".gpkg", driver='GPKG')