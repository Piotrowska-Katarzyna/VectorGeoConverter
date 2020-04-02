import os
from read_file.from_shp import from_shp

from read_file.from_geojson import from_geojson

from read_file.from_csv import from_csv

from write_file.to_geojson import to_geojson

from write_file.to_csv import to_csv

valid_formats = ["shapefile", "geojson", "csv"]
valid_extensions = [".shp", ".geojson", ".csv"]

def convert(file, target_format):
    filename, file_extension = os.path.splitext(file)
    if file_extension in valid_extensions and target_format in valid_formats:
        if file_extension == ".shp":
            gdf = from_shp(file)
        if file_extension == ".geojson":
            gdf = from_geojson(file)
        if file_extension == ".csv":
            gdf = from_csv(file, x = True, y = True)
        if target_format == "csv":
            to_csv(gdf, filename)
    else:
        print("niepoprawne dane wejściowe")