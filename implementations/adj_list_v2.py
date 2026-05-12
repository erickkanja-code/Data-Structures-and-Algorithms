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
    
def delete_node(v):
    graph.pop(v)
    for i in graph:
        if v in graph[i]:
            graph[i].remove(v)
            
def delete_edge(v1, v2):
    if v1 not in graph or v2 not in graph:
        return
    graph[v1].remove(v2)
    graph[v2].remove(v1)
    







graph = {}
add_node("a")
add_node("b")
add_node("c")
add_node("d")

add_edge("a", "b")
add_edge("a", "c")
print(graph)

delete_node("a")
print(graph)