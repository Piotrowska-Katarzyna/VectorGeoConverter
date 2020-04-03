import networkx as nx

def to_gml(gdf, filename):
    nx.to_file(filename, +".gml", driver = "GML")