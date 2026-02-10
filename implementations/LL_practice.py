#implement LL including the following operations:
#Traversal
#Add at the beginning, end and in-between(after and before a value)
#Delete from beginning, end, in-between and by-value

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node
            
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
    def add_after_value(self, data, x):
        if self.head is None:
            print(f"{x} not found!")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.ref
            if n is None:
                print(f"{x} is not found")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
                
    def add_before_value(self, data, x):
        if self.head is None:
            print(f"Value {x} not found")
        elif self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print(f"{x} not found in LL")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node            

        
        
        
    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head = self.head.ref
            
    def delete_end(self):
        if self.head is None:
            print("LL is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.ref is None:
                    break
                n = n.ref
            n.ref = None
          
    def delete_by_value(self, x):
        if self.head is None:
            print("LL is empty. Deletion cannot occur")
            return
        
        if self.head.data == x:
            self.head = self.head.ref
            return

        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Value is not found thus no deletion can occur")
        else:
            n.ref = n.ref.ref
            
        

    def traversal(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref
            print("None")
            
            
LL = LinkedList()

LL.add_begin(40)
LL.add_begin(30)
LL.add_begin(20)
LL.add_begin(10)
LL.traversal()
LL.delete_by_value(550)
LL.traversal()