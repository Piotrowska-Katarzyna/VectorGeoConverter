import numpy as np
import shapely
import topojson
import json


def from_topojson(file):
    tj = np.read_topojson(file)
    gdf = topojson.Topology(json, tj, prequantize=False, topology=True)
    #Zwracanie topologii TopoJSONa dla określonego obiektu geometrycznego
    #Topology(self, data, topology=True, prequantize=True, topoquantize=False, presimplify=False, toposimplify=0.0001, simplify_with='shapely', simplify_algorithm='dp', winding_order='CW_CCW')
    return gdf