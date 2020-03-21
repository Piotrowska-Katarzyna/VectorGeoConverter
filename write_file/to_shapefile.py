import geopandas as gpd 

def to_shapefile(gdf, filename):
     gdf.to_file(filename + ".shp")