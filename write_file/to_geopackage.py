import geopandas as gpd 

def to_gepackage(gdf, filename):
    gdf.to_file(filename + ".gpkg", driver='GPKG')