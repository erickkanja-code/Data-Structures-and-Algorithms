class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def print_LL(self):
        curr = self.head
        while curr is not None:
            print(curr.data, "-->", end=" ")
            curr = curr.ref
           
    def add_begin(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def reverse_LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            prev = None
            curr = self.head
            while curr is not None:
                next_node = curr.ref
                curr.ref = prev
                prev = curr
                curr = next_node
            self.head = prev
            
    
    
    
ll1 = LinkedList()

ll1.add_begin(2)
ll1.add_begin(1)
# ll1.print_LL()
ll1.reverse_LL()
ll1.print_LL()
