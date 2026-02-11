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

def delete_node(v):
    if v not in graph:
        print(f"{v} is not present in the graph")
        return
    graph.pop(v)
    for i in graph:
        for j in graph[i]:
            if v in j:
                graph[i].remove(j)
                break

def delete_edge(v1, v2):
    index1 = graph[v1].index(v2)
    index2 = graph[v2].index(v1)
    
    graph[v1].pop(index1)
    graph[v2].pop(index2)

graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A", "B", 10)
add_edge("B", "E", 3)
add_edge("A", "C", 5)
add_edge("A", "D", 4)
add_edge("B", "D", 7)
add_edge("C", "D", 1)
add_edge("E", "D", 2)
print(graph)

delete_node("C")
print(graph)
