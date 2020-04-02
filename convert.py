import os
from read_file.from_shp import from_shp

from read_file.from_geojson import from_geojson

from write_file.to_geojson import to_geojson

from write_file.to_shapefile import to_shapefile
from read_file.from_gml import from_gml
from write_file.to_gml import to_gml

valid_formats = ["shapefile", "geojson"]
valid_extensions = [".shp", ".geojson"]

def convert(file, target_format):
    filename, file_extension = os.path.splitext(file)
    if file_extension in valid_extensions and target_format in valid_formats:
        if file_extension == ".shp":
            gdf = from_shp(file)
        if target_format == "geojson":
            to_geojson(gdf, filename)
        if target_format == "shapefile":
            to_shapefile(gdf,filename)
        if file_extension == ".gml":
            gdf = from_gml(file)
        if target_format == "gml":
            to_gml(gdf, filename) 
    else:
        print("niepoprawne dane wejściowe")

convert("Województwa.shp", "shapefile") #gdy jest shp "niepoprawne...", gdy shapefile error

    elif file_extension in valid_extensions and target_format in valid_formats:
        if file_extension == ".geojson":
            gdf = from_geojson(file)
    else:
        print("niepoprawne dane wejściowe")
