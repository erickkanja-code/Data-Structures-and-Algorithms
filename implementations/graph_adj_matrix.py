def add_node(v):
    global node_count
    if v in nodes:
        print(f"{v} is present in nodes already")
    else:
        node_count += 1
        nodes.append(v)
        temp = []
        for row in graph:
            row.append(0) 
        for _ in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1, v2, cost):
    if v1 not in nodes or v2 not in nodes:
        return
    v1_index = nodes.index(v1)
    v2_index = nodes.index(v2)
    
    graph[v1_index][v2_index] = cost
    graph[v2_index][v1_index] = cost
    
def delete_node(v):
    global node_count
    if v not in nodes:
        print(f"{v} is not present in graph")
    else:
        index1 = nodes.index(v)
        nodes.pop(index1)
        node_count -= 1
        graph.pop(index1)
        for row in graph:
            row.pop(index1)
            
def delete_edge(v1, v2):
    if v1 not in nodes or v2 not in nodes:
        print("Either or both of the vertices are not in the graph")
        return
    index1 = nodes.index(v1)
    index2 = nodes.index(v2)
    graph[index1][index2] = 0
    graph[index2][index1] = 0
    

 
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"), end=" ")
        print()
        
nodes =[]
graph=[]
node_count = 0

add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 10)
add_edge("A", "C", 5)
print_graph()
delete_edge("A", "C")
print_graph()






