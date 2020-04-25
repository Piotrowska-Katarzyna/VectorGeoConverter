
def to_gml(gdf, filename):
    gdf.to_file(filename + ".gml", driver="GML")