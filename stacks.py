# stack = [10, 20, 30]
# # stack.append(10)
# # stack.append(20)
# # stack.append(30)
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())
# print(stack[len(stack)-1])

# stack = []
# def push():
#     element = input("Enter an element")
#     stack.append(element)
#     print(stack)
    
# def pop_element():
#     if not stack:
#         print("The stack cannot be popped as it is empty")
#     else:
#         removed_element = stack.pop()
#         print(removed_element)
#         print(stack)
        
# while True:
#     choice = int(input("Select an operation\n1.) Pushn2.) Pop\n3.) Quit"))
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop_element()
#     elif choice == 3:
#         break
#     else:
#         print("Choose either 1, 2 or 3")
# import collections

# stack = collections.deque()
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack[-1])
# print(stack)

# import queue

# stack = queue.LifoQueue(3)
# stack.put(10)
# stack.put(20)
# stack.put(30)
# stack.put(30, timeout=1)
# print(stack.get())

#PRACTICE

# stack = []
# #Push elements
# stack.append(10)
# stack.append(5)
# stack.append(589)
# print(stack)
# #Pop element
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack)

# #Top element
# #print(stack[-1])

# # if not stack:
# #     print("Stack is empty")
# # else:
# #     print("Stack has an element")
# import collections

# stack = collections.deque()
# #Push elements
# stack.append(10)
# stack.append(5)
# stack.append(589)
# print(stack)
# #Pop element

# stack.pop()
# print(stack)

# #Top element
# print(stack[-1])

# if not stack:
#     print("Stack is empty")
# # else:
#     print("Stack has an element")
    
import queue

stack2 = queue.LifoQueue(maxsize=3)

stack2.put(2, timeout=2)
stack2.put(3, timeout=2)
stack2.put(5, timeout=2)
print(stack2)

print(stack2.get())
print(stack2)
