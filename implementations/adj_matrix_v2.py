def add_node(v):
    global node_count
    if v in graph:
        print(f"{v} is already present in graph")
        return
    nodes.append(v)
    node_count += 1
    for row in graph:
        row.append(0)
    new_row = []
    for _ in range(node_count):
        new_row.append(0)
    graph.append(new_row)
    
def add_edge(v1, v2):
    if v1 not in nodes:
        print("Not possible")
        return
    if v2 not in nodes:
        print("Not possible")
        return
    index_v1 = nodes.index(v1)
    index_v2 = nodes.index(v2)
    
    graph[index_v1][index_v2] = 1
    graph[index_v2][index_v1] = 1
    
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"), end=" ")
        print()
        
        
def delete_node(v):
    global node_count
    if v not in nodes:
        print("Node not in graph")
        return
    index1 = nodes.index(v)
    removed_node = nodes.pop(index1)
    node_count -= 1
    for row in graph:
        row.pop(index1)
    graph.pop(index1)
    
def delete_edge(v1, v2):
    if v1 not in nodes:
        print("Not present")
        return
    if v2 not in nodes:
        print("Not present")
        return
    index_v1 = nodes.index(v1)
    index_v2 = nodes.index(v2)
    
    graph[index_v1][index_v2] = 0
    graph[index_v2][index_v1] = 0
    







graph = []
node_count = 0
nodes = []

add_node("a")
add_node("b")
add_node("c")
add_edge("b", "c")
delete_node("b")
print_graph()
print(nodes)
print(node_count)