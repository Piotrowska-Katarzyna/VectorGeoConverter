import pandas as pd
import geopandas as gpd


def from_csv(file, x, y):
    df = pd.read_csv(file)
    gdf = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df[x], df[y]))
    return gdf

#tesy, pozniej je usune stąd
mojedane = pd.read_csv("dane_wejsc\\csv.csv")
print(mojedane.head())
for col in mojedane.columns: 
    print(col)

gdf = gpd.GeoDataFrame(
    mojedane, geometry = gpd.points_from_xy(mojedane.longitude, mojedane.latitude))
print(gdf.head())