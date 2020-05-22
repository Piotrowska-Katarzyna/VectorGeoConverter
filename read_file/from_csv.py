import pandas as pd
import geopandas as gpd
from osgeo import ogr
from shapely import wkt

def from_csv(file, x = None, y = None, wkt1 = None):
    df = pd.read_csv(file)
    if x is not None and y is not None:
        gdf = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df[x], df[y]))
    elif wkt1 is not None:
        df[wkt1] = df[wkt1].apply(wkt.loads)
        gdf = gpd.GeoDataFrame(df, geometry= df[wkt1])
    return gdf

'''
#tesy, pozniej je usune stąd
mojedane = pd.read_csv("dane_wejsc\\csv.csv")
print(mojedane.head())
for col in mojedane.columns: 
    print(col)

gdf = gpd.GeoDataFrame(
   mojedane, geometry = gpd.points_from_xy(mojedane.longitude, mojedane.latitude))
print(gdf.head())

wkt = "POINT (1120351.5712494177 741921.4223245403)"
point = ogr.CreateGeometryFromWkt(wkt)
print(point.GetX(), point.GetY())

mojedane2 = pd.read_csv("dane_wejsc\\geojson.csv")
print(mojedane2.head())
for col in mojedane2.columns: 
    print(col)
'''
#druga opcja to wpisać coś na zasadzie "jeśli argumenty brane od uwagę to x, y to zrób to,
#jeśli argument brany pod uwagę to wkt to zrób to i to"

'''
def from_csv(file, x, y, wkt):
    df = pd.read_csv(file)
    gdf = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df[x], df[y]))
    df[wkt] = df[wkt].apply(wkt.loads)
    gdf2 = geopandas.GeoDataFrame(df, geometry= df[wkt])
    return gdf or gdf2 (wiem ze tak nie mozna chyba)
'''