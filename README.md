# VectorGeoConverter
<!-- badges: start -->
[![Version:v0.1](https://img.shields.io/github/v/release/Piotrowska-Katarzyna/VectorGeoConverter?include_prereleases)](https://github.com/Piotrowska-Katarzyna/VectorGeoConverter/releases/tag/v0.1)
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
* [Annotation](#annotation)
## Introduction 
This is a simple function called **convert()** created for conversion vector files between different formats. Currently, it works for 6 different formats and acquire features like giving specific path for saving a new file and choosing filename for a new file. 
#### Technologies
Python 3.8.1; required packages/modules:
* geopandas
* pandas
* os
* numpy
* json
* shapely
#### Structure
Convert.py file contains function convert() and this is the function that converts files. 
Here is a structure of this function:
```python 
convert(from_file, to_format, to_file=None, epsg=None, csv_geo_columns=None)
```
Parameters: 
* **from_file**: str, path object or file-like object <br />
File one's ueses for conversion.
* **to_format**: str <br />
Format one's wants to convert a primary file. 
* **to_file**: str, desired path object or/and new file name, default ``None`` <br />
An optional argument. New name for converted file. By default, new file will be saved in the same place, where python file (in which conversion happens) currently is. For choosing a specific place on your device, additionally put in desired path in this argument. 
* **epsg**: int, default ``None`` <br />
An optional argument. 
* **csv_geo_columns**: list, default ``None``<br />
An optional argument, yet needed for converting CSV format to any other. List of column name(s) containing geometry. Works for having coordinates in two columns and WKT format.
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

## Annotation
If you want to convert data containing information about date, most likely convert() function will change date data type to a string. Please have that in mind if dates in your data are important for further work. 
