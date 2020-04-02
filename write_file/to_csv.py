import pandas as pd 

def to_csv(gdf, filename):
    gdf.to_csv(filename + '.csv')
