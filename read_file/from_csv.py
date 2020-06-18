import pandas as pd
import geopandas as gpd
from osgeo import ogr
from shapely import wkt

def from_csv(file, csv_geo_columns):
    if csv_geo_columns is not None and isinstance(csv_geo_columns, list):
        df = pd.read_csv(file)
        if len(csv_geo_columns) == 1:
            wkt_col = csv_geo_columns[0]
            df[wkt_col] = df[wkt_col].apply(wkt.loads)
            gdf = gpd.GeoDataFrame(df, geometry= df[wkt_col])
        elif len(csv_geo_columns) == 2:
            x_col = csv_geo_columns[0]
            y_col = csv_geo_columns[1]
            gdf = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df[x_col], df[y_col])) 
        return gdf