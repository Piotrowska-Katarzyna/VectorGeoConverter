import numpy as np
import topojson

def to_topojson(gdf, filename):
    gdf.to_topojson(filename + '.topojson')