import numpy as np
import topojson
import json

def to_topojson(gdf, filename):
    tj = topojson.Topology(gdf, prequantize=False, topology=True)
    string_json = tj.to_json()

    #Zapis do pliku
    text_file = open(filename + ".topojson", "w")
    text_file.write(string_json)
    text_file.close()