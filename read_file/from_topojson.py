import numpy as np
import shapely
import topojson
import json


def from_topojson(file):
    tj = np.read_topojson(file)
    gdf = topojson.Topology(json, tj, prequantize=False, topology=True)
    return gdf