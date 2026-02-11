def add_node(v):
    if v in graph:
        print(f"{v} in graph already")
    else:
        graph[v] = []
        
def add_edge(v1, v2):
    if v1 not in graph or v2 not in graph:
        print("Element missing from graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def delete_node(v):
    if v not in graph:
        print(f"{v} is not present in the graph")
        return
    graph.pop(v)
    for i in graph:
        if v in graph[i]:
            graph[i].remove(v)

def delete_edge(v1, v2):
    index1 = graph[v1].index(v2)
    index2 = graph[v2].index(v1)
    
    graph[v1].pop(index1)
    graph[v2].pop(index2)

graph = {}
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B")
add_edge("A", "C")
print(graph)

delete_edge("A","B")
print(graph)
