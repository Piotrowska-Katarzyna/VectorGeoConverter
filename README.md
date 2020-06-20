# VectorGeoConverter
## Table of contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [How to use](#how-to-use)
* [Structure](#structure)
* [Examples of use](#examples-of-use)
* [Project status](#project-status)
## Introduction 
This is a simple tool created for conversion vector files between different formats. 
## Technologies
Python 3.8.1 - czy wypisywać też pakiety?
#### nie wiem jak to nazwac ale:
## How to use / Launge / Installation 
You can use the convert() function by cloning or downloading files from this repository and opening it in desired IDE or code editor. 
## Structure
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
## Examples of use
Here are some examples of use:
```python
convert(from file = 'file.shp', to_format = 'geojson', to_file = 'file2')
convert('data.csv', 'gml', 2180 , [lon, lat])
convert('data.csv', 'gml', 'path\\conv_data', epsg = 4326 , csv_geo_column = [wkt_geom])
```
## Project status 
This project is: _in progress_. Feel free to test this function and give us feedback. 
