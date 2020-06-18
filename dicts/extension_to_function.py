from read_file.from_shp import from_shp
from read_file.from_geojson import from_geojson
from read_file.from_csv import from_csv
from read_file.from_gml import from_gml
from read_file.from_topojson import from_topojson
from read_file.from_geopackage import from_geopackage

from write_file.to_geojson import to_geojson
from write_file.to_shp import to_shp
from write_file.to_geopackage import to_geopackage
from write_file.to_csv import to_csv
from write_file.to_gml import to_gml
from write_file.to_csv import to_csv
from write_file.to_topojson import to_topojson

extension_to_read_function = {
    ".shp" : from_shp,
    ".gml" : from_gml,
    ".csv" : from_csv,
    ".geojson" : from_geojson,
    ".topojson" : from_topojson,
    ".gpkg" : from_geopackage
}

extension_to_write_function = {
    ".shp" : to_shp,
    ".gml" : to_gml,
    ".csv" : to_csv,
    ".geojson" : to_geojson,
    ".topojson" : to_topojson,
    ".gpkg" : to_geopackage
}