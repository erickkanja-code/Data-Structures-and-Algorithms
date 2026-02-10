# class BST:
#     def __init__(self, key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None
        
#     def insert(self, data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key == data:
#             return
#         if self.key > data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = BST(data)
#         else: 
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = BST(data)
    
#     def search(self, data):
#         if self.key is None:
#             print("Node is not present in tree")
#             return
#         if self.key == data:
#             print("Node is found")
#         elif self.key > data:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("Node is not present in tree")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("Node is not present in tree")
    
#     def preorder(self):
#         print(self.key, end =" ")
#         if self.lchild:
#             self.lchild.preorder()
#         if self.rchild:
#             self.rchild.preorder()
            
#     def inorder(self):
#         if self.lchild:
#             self.lchild.inorder()
#         # print("In-order traversal")
#         print(self.key, end= "/n")
#         if self.rchild:
#             self.rchild.inorder()  
            
#     def postorder(self):
#         if self.lchild:
#             self.lchild.postorder()
#         if self.rchild:
#             self.rchild.postorder()
#         print(self.key) 
        
#     def delete(self, data, curr):
#         if self.key is None:
#             print("Tree is empty: Node not found")
#             return
#         if self.key < data:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(data)
#             else:
#                 print("Node not found")
#         elif self.key > data:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(data)
#             else:
#                 print("Node not found")
#         else:
#             if self.lchild is None:
#                 temp = self.rchild
#                 if data == curr:
#                     self.key = temp.key
#                     self.lchild = temp.lchild
#                     self.rchild = temp.rchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
#             if self.rchild is None:
#                 temp = self.lchild
#                 if data == curr:
#                     self.key = temp.key
#                     self.rchild =temp.rchild
#                     self.lchild = temp.lchild
#                     temp = None
#                     return
#                 self = None
#                 return temp
#             node = self.rchild 
#             while node.lchild:
#                 node = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(node.key)
            
#         return self
    
#     def minimum(self):
#         node = self
#         while node.lchild:
#             node = node.lchild
#         print("\n", node.key)
            
    
#     def maximum(self):
#         node = self
#         while node.rchild:
#             node = node.rchild
#         print("\n", node.key)
            
        
        
        
        
# def count(node):
#     if node is None:
#         return 0
#     return 1 + count(node.lchild) + count(node.rchild)
            
    
# root = BST(10)
# lis1 = [37,30]

# for num in lis1:
#     root.insert(num)
# print("Pre-order traversal")    
# root.preorder() 
# root.minimum()
# root.maximum()

class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
             return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else: 
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        if self.key is None:
            print(f"{data} not found: BST is empty")
            return
        if self.key == data:
            print(f"{data} is present in the BST")
        elif self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Value is not present in BST")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Value is not present in BST")
    
    def preorder(self):
        print(self.key,  end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()
            
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key)
        
    def delete(self, data, curr):
        if self.key is None:
            print(f"{data} not present in BST")
            return
        if self.key > data:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print(f"{data} not present in BST")
        elif self.key < data:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print(f"{data} not present in BST")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.rchild = temp.rchild
                    self.lchild = temp.lchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.rchild = temp.rchild
                    self.lchild = temp.lchild
                    temp = None
                    return
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node  = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self
    
    def min_node(self):
        node = self
        while node.lchild:
            node = node.lchild
        return node.key
            
    def max_node(self):
        node = self
        while node.rchild:
            node = self.rchild
        return node.key
                

def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)
          
root = BST(10)

list1 = [6, 3, 1, 6, 98, 3, 7]
for i in list1:
    root.insert(i)
# root.preorder()

# if count(root) > 1:
#     root.delete(10, root.key)
# else:
#     print("Can't perform deletion")


# root.preorder()
print(root.max_node())
print(root.min_node())