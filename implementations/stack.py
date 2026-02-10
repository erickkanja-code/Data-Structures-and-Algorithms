#Implementing a stack usinga list

stack = []

# Push elements
stack.append(20)
stack.append(10)
stack.append(30)

print(stack)

# Pop elements
popped_element = stack.pop()
print(popped_element)
print(stack)

# Top of the stack
print(stack[-1])

# isEmpty
if not stack:
    print("Stack is empty")
else:
    print("Stack has elements")