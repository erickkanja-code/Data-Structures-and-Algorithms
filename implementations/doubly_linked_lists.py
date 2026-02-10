class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None
        
class DoublyLL:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.nref
    
    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.pref
    
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node              
        else:
            print("Linked List is not empty!")
    def add_begin(self, data):
        if self.head is None:
           new_node = Node(data)
           self.head = new_node
        else:
            new_node = Node(data)
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
    
    def add_after(self, data, x):
        if self.head is None:
            print("LL is empty, cannot add after")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                else:
                    n = n.nref
            if n is None:
                print("Value is not present")
            else:
                new_node = Node(data)
                if n.nref is None:
                    new_node.pref = n
                    n.nref = new_node
                    return
                n.nref.pref = new_node
                new_node.nref = n.nref
                new_node.pref = n
                n.nref =  new_node
    def add_before(self, data, x):
        if self.head is None:
            print("LL is empty, cannot add after")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Value is not present")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node
                
    def delete_begin(self):
        if self.head is None:
            print("LL is empty thus we cannot delete a node")
        elif self.head.nref is None:
            self.head = None
        else:
            n = self.head
            self.head = n.nref
            self.head.pref = None      
    def delete_end(self):
        if self.head is None:
            print("LL is empty thus we can't delete from end")
        elif self.head.nref is None:
            self.head = None
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None
    def delete_by_value(self, x):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.nref is None:
            if x == self.head.data:
                self.head = None
            else:
                print("Value isn't present")
        elif self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
        else:
            n = self.head
            while n.nref is not None:
                if n.data == x:
                    break
                n = n.nref
            if n.nref is None:
                if n.data == x:
                    n.pref.nref = None
                else:
                    print("Value is not present")
            else:
                n.pref.nref  = n.nref
                n.nref.pref = n.pref
                    
            
            
            
            
            
dl1 = DoublyLL()
dl1.add_begin(4)
dl1.add_end(8)
# dl1.add_end(12)
dl1.delete_by_value(190)

dl1.print_LL()
