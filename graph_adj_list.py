def add_node(v):
    if v in graph:
        print(f"{v} in graph already")
    else:
        graph[v] = []
        
def add_edge(v1, v2, cost):
    if v1 not in graph or v2 not in graph:
        print("Element missing from graph")
    else:
        graph[v1].append([v2, cost])
        graph[v2].append([v1, cost])




graph = {}
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 100)
add_edge("A", "C", 50)
print(graph)

