import os
from read_file.from_shp import from_shp
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

# z shapefile na geojson
convert("dane_wejsciowe\Województwa.shp", "geojson")
# z geojson na shapefile
convert("dane_wejsciowe\map.geojson", "shapefile")