import collections

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
        
def shortest_path(start, target, visited):
    
        
graph = {}
visited = {}

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")
add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "D")
add_edge("C", "D")
add_edge("F", "E")
add_edge("F", "G")