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

valid_extensions = [".shp", ".geojson", ".gpkg", ".csv", ".topojson", ".gml"]
valid_formats = {
    'shapefile':'shapefile',
    'shp':'shapefile',
    '.shp':'shapefile',
    'esri shapefile':'shapefile',
    'esri':'shapefile',
    'esri shp':'shapefile',
    'geojson':'geojson',
    'geo json':'geojson',
    '.geojson':'geojson',
    'gjson':'geojson',
    'geopackage':'geopackage',
    'gpkg':'geopackage',
    '.geopackage':'geopackage',
    '.gpkg':'geopackage',
    'geopaczka':'geopackage',
    'csv':'csv',
    '.csv':'csv',
    'comma-separated values':'csv',
    'comma separated values': 'csv',
    'topojson':'topojson',
    'topo json':'topojson',
    '.topojson':'topojson',
    'tjson':'topojson',
    'topology json':'topojson',
    'gml':'gml',
    '.gml':'gml',
    'geography markup language':'gml'
    }

def convert(file, target_format, new_file=None, epsg=None, csv_options=None):
    filename, file_extension = os.path.splitext(file)
    new_dir = ''
    if new_file is not None: 
        new_dir, new_filename = os.path.split(new_file)
        if isinstance(new_filename, str):
            filename = new_filename
        else:
            filename = str(new_filename)
    if file_extension in valid_extensions and target_format.lower() in valid_formats:
        if file_extension == ".shp":
            gdf = from_shp(file)
        if file_extension == ".geojson":
            gdf = from_geojson(file)
        if file_extension == ".gpkg":
            gdf = from_geopackage(file) 
        if file_extension == ".csv":
            gdf = from_csv(file, csv_options)
        if file_extension == ".gml":
            gdf = from_gml(file)
        if file_extension == ".topojson":
            gdf = from_topojson(file)

        if gdf.crs is not None:
            if epsg is not None and gdf.crs != f'EPSG:{epsg}':
                #error
                pass
        else: 
            if epsg is None:
                gdf.crs = "EPSG:4326"
            else:
                gdf.crs = f'EPSG:{epsg}'
        
        if new_dir != '':
            os.chdir(new_dir)

        target_format_validated = valid_formats.get(target_format.lower())
        if target_format_validated == "csv":
            to_csv(gdf, filename)
        if target_format_validated == "geojson":
            to_geojson(gdf, filename)
        if target_format_validated == "geopackage":
            to_geopackage(gdf, filename)
        if target_format_validated == "shapefile":
            to_shapefile(gdf, filename)
        if target_format_validated == "gml":
            to_gml(gdf, filename) 
        if target_format_validated == "topojson":
            to_topojson(gdf, filename)

    else:
        print("niepoprawne dane wejściowe")
