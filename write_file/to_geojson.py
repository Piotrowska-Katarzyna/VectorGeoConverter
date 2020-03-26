import geopandas as gpd 

def to_geojson(gdf, filename):
    gdf.to_file(filename + ".geojson", driver='GeoJSON')