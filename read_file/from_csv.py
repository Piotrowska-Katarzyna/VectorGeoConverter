import pandas as pd
import geopandas as gpd


def from_csv(file, x, y):
    df = pd.read_csv(file)
    gdf = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df[x], df[y]))
    return gdf