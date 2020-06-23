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
Python 3.6+ ; required packages/modules:
* geopandas
* pandas
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
File one's uses for conversion.
* **to_format**: str <br />
Format one's wants to convert a primary file. 
* **to_file**: str, desired path object or/and new file name, default ``None`` <br />
An optional argument. New name for converted file. By default, new file will be saved in the same place, where python file (in which conversion happens) currently is and will have the same name as input file (but with diffrent extension). For choosing a specific place on your device or specific filename, additionally put in desired path in this argument. 
* **epsg**: int, default ``None`` <br />
An optional argument. EPSG is an id that represents coordinate systems - check http://epsg.io/ for more examples! Also note that some formats, like shp, might contain informations about epsg in metadata. In such cases there is no need to fill epsg argument manually. If there is no epsg stated by user and algorythm cannot read it from metadata, output will be saved in default EPSG:4326 coordinates ( http://epsg.io/4326 ). 
Notice that Convert() DO NOT perform any transformations, which means you state here the epsg of input file. EPSG of input and output files should be always the same. 
* **csv_geo_columns**: list, default ``None``<br />
An optional argument, yet needed for converting CSV format to any other. List of column name(s) containing geometry. Works for having coordinates in two columns (X, Y) or one (WKT). You CANNOT read csv file without pointing to spatial column(s) in this argument.
## Supported formats
Currently, function convert() works with 6 formats:
* ESRI Shapefile
* Geography Markup Language (GML)
* GeoJSON
* TopoJSON
* GeoPackage
* Comma-separated values (CSV)
## How to use 
You can use the convert() function by cloning or downloading files from this repository and opening it in desired IDE or code editor. 
## Examples of use
Here are some examples of use:
```python
# Simple shapefile (stored in local path input_data/) to GeoJSON conversion - without any optional arguments. This will save the file in working directory as 'file.geojson'
# EPSG will be either read from .prj or, if such file won't be find, will be set to default 4326.
convert(from file = 'input_data/file.shp', to_format = 'geojson')

# Same shapefile (stored in local path input_data/) to GeoJSON conversion, but with arguments - we want to save new file as "awesomefile.geojson" in output_data/ path
convert(from file = 'input_data/file.shp', to_format = 'geojson', to_file='output_data/awesomefile', epsg = 2180)

# CSV to GML conversion, notice the usage of csv_geo_columns argument - lon and lat are colnames in csv containing spatial data
convert(from file = 'data.csv', to_format = 'gml', to_file='newdata', epsg = 2180 , csv_geo_columns = ['lon', 'lat'])
```
## Project status 
This project is: _in progress_. Feel free to test this function and give us feedback. 

## Annotation
If you want to convert data containing information about date, most likely convert() function will change date data type to a string. Please have that in mind if dates in your data are important for further work. 
