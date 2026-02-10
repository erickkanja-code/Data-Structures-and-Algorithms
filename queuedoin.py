# queue = []

# def enqueue(x, max_length):
#     if len(queue) == max_length:
#         print("Queue is full")
#     else:
#         queue.append(x)
#         print(f"New queue: {queue}")
    
# def dequeue():
#     if not queue:
#         print("Queue is empty")
#     else:
#         removed_element = queue.pop(0)
#         print(f"{removed_element} has been removed. The new queue is {queue}")
        
# max_length = int(input("What's the limit of elements?"))
# while True:
#     selection = int(input("Select an option: 1.Enqueue 2.Dequeue 3.Quit"))
#     if selection == 1:
#         element = input("Enter an element:")
#         enqueue(element, max_length)
#     elif selection == 2:
#         dequeue()
#     elif selection == 3:
#         break
#     else:
#         print("Enter one of the 3 options")

# import collections

# queue = collections.deque()

# queue.append(20)
# queue.append(10)
# queue.append(5)

# import queue

# queue = queue.Queue(maxsize=3)

# queue.put(10)
# queue.put(20)
# queue.put(30)
# #queue.put(30, timeout=1)
# print(queue)


# Priority Queue
# q = []
# q.append(10)
# q.append(40)
# q.sort()
# q.append(20)
# q.sort()
# print(q)
# print(q.pop(0))
# print(q.pop(0))
# print(q.pop(0))
# #print(q.pop(0))

import queue
q = queue.PriorityQueue()
q.put(10)
q.put(60)
q.put(20)
q.put(40)
q.put(40)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())

queue2 = [(3, "Erick"), (2, "Simon"), (1, "Peter")]
queue2.sort()

for t in queue2:
    print(t[1])