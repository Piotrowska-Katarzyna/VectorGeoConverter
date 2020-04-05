import networkx as nx

def from_gml(file):
    gdf = nx.read_file(file)
    return gdf

