import os
from read_file.from_shp import from_shp
from write_file.to_geojson import to_geojson
valid_formats = ["shapefile", "geojson"]
valid_extensions = [".shp", ".geojson"]

def convert(file, target_format):
    filename, file_extension = os.path.splitext(file)
    if file_extension in valid_extensions and target_format in valid_formats:
        if file_extension == ".shp":
            gdf = from_shp(file)
        if target_format == "geojson":
            to_geojson(gdf, filename)
    else:
        print("niepoprawne dane wejściowe")

convert("Województwa.shp", "geojson")