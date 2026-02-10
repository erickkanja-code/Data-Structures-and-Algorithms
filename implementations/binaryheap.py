# import heapq

# # heap = []
# # heapq.heappush(heap, 10)
# # heapq.heappush(heap, 1)
# # heapq.heappush(heap, 5)
# # min = heapq.heappop(heap)
# # print(heap)
# # print(min)
# import heapq
# list1 = [2,3,5,7,4,6]

# heapq.heapify(list1)
# print(list1)

# # min = heapq.heappushpop(list1, 1)
# # print(list1)
# # print(min)

# # heapq.heapreplace(list1, 1)
# # print(list1)

# heap = [1, 20, 5, 4, 3, 6, 2]
# new_heap = heapq.heapify(heap)
# min = heapq.nsmallest(2, heap, key=None)
# print(min)
# print(heap) 
# import heapq


# # print(heapq.nsmallest(4, heap))

# list1 = [(1, "ria"), (4, "sia"), (3, "gia")]

# heapq.heapify(list1)
# print(list1)

# print(heapq.heappop(list1))
# print(heapq.heappop(list1))
# print(heapq.heappop(list1))
import heapq

list1 = [10, 30, 70, 50, 100, 1, 50, 40]
print(heapq.nlargest(3, list1))