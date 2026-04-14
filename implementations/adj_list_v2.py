def add_node(v):
    if v in graph:
        print("Node is already present")
        return
    graph[v] = []
    
def add_edge(v1, v2):
    if v1 not in graph or v2 not in graph:
        print("Values not in graph")
        return
    graph[v1].append(v2)
    graph[v2].append(v1)
    







graph = {}