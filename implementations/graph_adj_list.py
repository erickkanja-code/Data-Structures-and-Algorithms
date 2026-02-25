import collections

def add_node(v):
    if v in graph:
        print(f"{v} in graph already")
    else:
        graph[v] = []
        # reversed_graph[v] = []
        
def add_edge(v1, v2):
    if v1 not in graph or v2 not in graph:
        print("Element missing from graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
        # reversed_graph[v2].append(v1)

# def delete_node(v):
#     if v not in graph:
#         print(f"{v} is not present in the graph")
#         return
#     graph.pop(v)
#     for i in graph:
#         for j in graph[i]:
#             if v in j:
#                 graph[i].remove(j)
#                 break

# def delete_edge(v1, v2):
#     if v2 in graph[v1]:
#         index1 = graph[v1].index(v2)
#         index2 = graph[v2].index(v1)
#         graph[v1].pop(index1)
#         graph[v2].pop(index2)
        
    # temp = [v1, cost]
    # temp1 = [v2, cost]
    # if temp1 in graph[v1]:
    #     graph[v1].remove(temp1)
    #     graph[v2].remove(temp)


def DFS_recursive(node, visited, graph):
    if node not in graph:
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            DFS_recursive(neighbor, visited, graph)














def BFS(node, visited1, graph):
    if node not in graph:
        print("The node is not present")
        return
    if node not in visited1:
        Queue = collections.deque()
        Queue.append(node)
        visited1.add(node)
        while Queue:
            current = Queue.popleft()
            print(current)
            for neighbor in graph[current]:
                if neighbor not in visited1:
                    Queue.append(neighbor)
                    visited1.add(neighbor)
                    



# def DFS_iterative(node, visited, graph):
#     if node not in graph:
#         print("Node is not present in graph")
#         return
#     if node in visited:
#         return
#     stack = []
#     stack.append(node)
#     while stack: 
#         current = stack.pop()
        
#         if current not in visited:
#             print(current)
#             visited.add(current)
#             for i in graph[current]:
#                 stack.append(i)

        
    
    
visited=set()
visited1=set()
graph = {}

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")


add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "D")
add_edge("C", "D")
add_edge("B", "E")
add_edge("E", "D")
add_edge("D", "F")

print(graph)
DFS_recursive("A", visited, graph)

# print("BFS")
# BFS("A", visited1, graph)

# for i in list(graph):
#     if i not in visited:
#         print("Weakly connected graph")
#         break
# else:
#     DFS_recursive("A", visited1, reversed_graph) 
#     if visited == visited1:
#         print("strongly connected graph")
#     else:
#         print("weakly connected graph")
    
    
    

    
