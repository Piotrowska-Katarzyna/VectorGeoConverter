import pandas as pd 
import os

def to_csv(gdf, file):
    file_name, file_extension = os.path.splitext(file)
    if file_extension == '':
        full_file = file_name + ".csv"
    else:
        full_file = file
    gdf.to_csv(full_file)
