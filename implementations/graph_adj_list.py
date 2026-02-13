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
        for j in graph[i]:
            if v in j:
                graph[i].remove(j)
                break

def delete_edge(v1, v2):
    if v2 in graph[v1]:
        index1 = graph[v1].index(v2)
        index2 = graph[v2].index(v1)
        graph[v1].pop(index1)
        graph[v2].pop(index2)
        
    # temp = [v1, cost]
    # temp1 = [v2, cost]
    # if temp1 in graph[v1]:
    #     graph[v1].remove(temp1)
    #     graph[v2].remove(temp)

graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A", "B")
add_edge("B", "E")
add_edge("A", "C")
add_edge("A", "D")
add_edge("B", "D")
add_edge("C", "D")
add_edge("E", "D")
print(graph)

delete_edge("B", "E")
print(graph)
