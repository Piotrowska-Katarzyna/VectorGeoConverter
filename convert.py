import os

from read_file.from_shp import from_shp
from read_file.from_geojson import from_geojson
from read_file.from_csv import from_csv
from read_file.from_gml import from_gml
from read_file.from_topojson import from_topojson
from read_file.from_geopackage import from_geopackage

from write_file.to_geojson import to_geojson
from write_file.to_shapefile import to_shapefile
from write_file.to_geopackage import to_geopackage
from write_file.to_csv import to_csv
from write_file.to_gml import to_gml
from write_file.to_csv import to_csv
from write_file.to_topojson import to_topojson

valid_formats = ["shapefile", "geojson", "geopackage", "csv"]
valid_extensions = [".shp", ".geojson", ".gpkg", ".csv"]

def convert(file, target_format, x = None, y = None, wkt = None):
    filename, file_extension = os.path.splitext(file)
    if file_extension in valid_extensions and target_format in valid_formats:
        if file_extension == ".shp":
            gdf = from_shp(file)
        if file_extension == ".geojson":
            gdf = from_geojson(file)
        if file_extension == ".gpkg":
            gdf = from_geopackage(file) 
        if file_extension == ".csv":
            if x != None and y != None:
                gdf = from_csv(file, x, y)
            elif wkt != None:
                gdf = from_csv(file, wkt)
        if file_extension == ".gml":
            gdf = from_gml(file)
        if file_extension == ".topojson":
            gdf = from_topojson(file)

        if target_format == "csv":
            to_csv(gdf, filename)
        if target_format == "geojson":
            to_geojson(gdf, filename)
        if target_format == "geopackage":
            to_geopackage(gdf, filename)
        if target_format == "shapefile":
            to_shapefile(gdf, filename)
        if target_format == "gml":
            to_gml(gdf, filename) 
        if target_format == "topojson":
            to_topojson(gdf, filename)

    else:
        print("niepoprawne dane wejściowe")
