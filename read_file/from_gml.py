import networkx as nx

def from_gml(file):
    nx = nx.read_file(file)
    return nx

