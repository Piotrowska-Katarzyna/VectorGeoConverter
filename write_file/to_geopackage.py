import geopandas as gpd
import os

def to_geopackage(gdf, file):
    file_name, file_extension = os.path.splitext(file)
    if file_extension == '':
        full_file = file_name + ".gpkg"
    else:
        full_file = file
    gdf.to_file(full_file, driver='GPKG')