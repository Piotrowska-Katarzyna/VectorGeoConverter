import os
from dicts.extension_to_function import extension_to_read_function, extension_to_write_function
from dicts.valid_formats import valid_formats

valid_extensions = [".shp", ".geojson", ".gpkg", ".csv", ".topojson", ".gml"]

def convert(from_file, to_format, to_file=None, epsg=None, csv_geo_columns=None):
    filename, file_extension = os.path.splitext(from_file) 
    new_dir = ''
    if to_file is not None: 
        new_dir, to_filename = os.path.split(to_file)
        if isinstance(to_filename, str):
            filename = to_filename
        else:
            filename = str(to_filename)

    if ~isinstance(epsg, int) and epsg is not None: 
        raise Exception(f'EPSG parameter must be {type(1)} , but is {type(epsg)} instead')

    if file_extension in valid_extensions and to_format.lower() in valid_formats:
        
        read_function = extension_to_read_function.get(file_extension)
        gdf = read_function(from_file, csv_geo_columns)

        if gdf.crs is not None:
            if epsg is not None and gdf.crs["init"] != f'epsg:{epsg}':
                raise Exception(f'EPSG given (epsg:{epsg}) is different from EPSG detected from file ({gdf.crs["init"]})')
        else: 
            if epsg is None:
                gdf.crs = "EPSG:4326"
            else:
                gdf.crs = f'EPSG:{epsg}'
        
        if new_dir != '':
            os.chdir(new_dir)

        target_format_validated = "."+valid_formats.get(to_format.lower())
        write_function = extension_to_write_function.get(target_format_validated)
        write_function(gdf, to_file)

    elif file_extension.lower() in [".json", "json"]:
        raise Exception("Extention .json is ambiguous. At this instant convert() \
function can handle .geojson and .topojson extensions. Please change your file extension to one of those.")
    elif to_format.lower() in [".json", "json"]:
        raise Exception("Extention .json is ambiguous. At this instant convert() \
function can handle .geojson and .topojson extensions. Please change to_format paremeter to one of those.")
    else:
        if file_extension not in valid_extensions:
            raise Exception(f"File extension {file_extension} is not handled by convert().")
        else:   
            raise Exception(f"File extension in to_format parameter {to_format} is not handled by convert().")
