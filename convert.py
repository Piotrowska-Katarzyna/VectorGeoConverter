import os
from read_file.from_shp import from_shp

from read_file.from_geojson import from_geojson

from write_file.to_geojson import to_geojson

valid_formats = ["shapefile", "geojson"]
valid_extensions = [".shp", ".geojson"]

def convert(file, target_format):
    filename, file_extension = os.path.splitext(file)
    if file_extension in valid_extensions and target_format in valid_formats:
        if file_extension == ".shp":
            gdf = from_shp(file)

    elif file_extension in valid_extensions and target_format in valid_formats:
        if file_extension == ".geojson":
            gdf = from_geojson(file)
    else:
        print("niepoprawne dane wejściowe")