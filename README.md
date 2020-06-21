# VectorGeoConverter
<!-- badges: start -->
[![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
<!-- badges: end -->
## Table of contents
* [Introduction](#introduction)
  * [Technologies](#technologies)
  * [Structure](#structure)
* [Supported formats](#supported-formats)
* [How to use](#how-to-use)
* [Examples of use](#examples-of-use)
* [Project status](#project-status)
## Introduction 
This is a simple tool created for conversion vector files between different formats. 
#### Technologies
Python 3.8.1 - czy wypisywać też pakiety?
#### Structure
Convert.py file contains function convert() and this is the function that converts files. 
Here is a structure of this function:
```python 
convert(from_file, to_format, to_file=None, epsg=None, csv_geo_columns=None)
```
Parameters: 
* from_file: str, path object or file-like object
* to_format: str
* to_file: str, desired path object or/and new file name, default ``None``
* epsg: int, default ``None``
* csv_geo_columns: list, default ``None``
List of column names to use.
## Supported formats
Currently, function convert() works with 6 formats:
* ESRI Shapefile
* Geography Markup Language (GML)
* GeoJSON
* TopoJSON
* GeoPackage
* comma-separated values (CSV)
## How to use 
You can use the convert() function by cloning or downloading files from this repository and opening it in desired IDE or code editor. 
## Examples of use
Here are some examples of use:
```python
convert(from file = 'file.shp', to_format = 'geojson', to_file = 'file2') # Shapefile to GeoJSON conversion and changing filename
convert(from file = 'data.csv', to_format = 'gml', epsg = 2180 , csv_geo_columns = [lon, lat]) # CSV to GML conversion without changing filename, adding information about EPSG and columns with geometry
convert(from file = 'data.csv', to_format = 'gpkg', to_file = 'conv_data', epsg = 4326 , csv_geo_column = [wkt_geom]) # CSV to GeoPackage conversion, changing filename, adding information about EPSG and column with geometry
```
## Project status 
This project is: _in progress_. Feel free to test this function and give us feedback. 
