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








graph = []
node_count = 0
nodes = []

add_node("a")
add_node("b")
add_node("c")
print(graph)
print(nodes)
print(node_count)