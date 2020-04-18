import numpy as np
import topojson
import json

def to_topojson(gdf, filename):
    gdf.to_topojson(filename + '.topojson')