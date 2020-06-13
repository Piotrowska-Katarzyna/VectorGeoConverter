import numpy as np
import topojson
import json
import os

def to_topojson(gdf, file):
    file_name, file_extension = os.path.splitext(file)
    if file_extension == '':
        full_file = file_name + ".topojson"
    else:
        full_file = file
    tj = topojson.Topology(gdf, prequantize=False, topology=True)
    string_json = tj.to_json()

    #Zapis do pliku
    text_file = open(full_file, "w")
    text_file.write(string_json)
    text_file.close()