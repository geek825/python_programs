'''
class Node :
    def __init__(self , data):
        self.data =  data
        self.head = None

class Linkedlist:
    def __init__(self , data):
        self.head =  None

    def travers(self , data):
        if self.head is None:
            print("Linked list is empty")
        curr = self.head
        while curr:
            print(curr.data, end="-->")

    def add_empty(self , data):
        new_node  = Node(data)
        if self.head is not None:
            self.head = new_node
        else:
            print("Linkes list is not empty")

    def add_begain(self , data):
        new_node = Node(data)
        if self.head is None :
            self.head =  new_node
        else:
            new_node.next =  self.data
            self.data.prev = new_node 
            self.data = new_node
l1 =  Linkedlist()
l1.add_begain(10)
l1.travers()
'''   


def reverse(self , data):
    prev = None
    curr = self.head 
    while curr:
        new_node = curr.next
        curr.next = prev
        curr = prev 
        curr = new_node 
    return prev
    
# # class Node:
# #     def __init__(self , data):
# #         self.data = data
# #         self.next = None
        
# # class Linkedlist:
# #     def __init__(self):
# #         self.head  = None
    
# #     def travers(self):
# #         curr = self.head
        
# #         while curr :
# #             print(curr.data , end=" --> ")
# #             curr = curr.next 
# #         print("None")
            
# #     def add_begain(self , data):
# #         new_node =  Node(data)
# #         new_node.next = self.head
# #         self.head = new_node 
        
# #     def add_end(self , data):
# #         new_node = Node(data)
# #         if self.head is None:
# #             self.head = new_node
# #             return 
        
# #         curr = self.head
# #         while curr.next:
# #             curr = curr.next
# #         curr.next = new_node
            
# # li = Linkedlist()
# # li.add_begain(20)
# # li.add_end(10)
# # li.travers()


# # def bubble_sort(arr):
# #     for i in range(len(arr)-1):
# #         for j in range(len(arr)-1-i):
# #             if arr[j] > arr[j+1]:
# #                 arr[j],arr[j+1] = arr[j+1], arr[j]
# # arr = [12,11,1,22,34,4]
# # bubble_sort(arr)
# # print(arr)


# class BST:
#     def __init__(self , key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None
        
#     def insert(self , data):
#         if self.key is None:
#             return 
#         if data == self.key:
#             return 
        
#         if data < self.key:
#             if self.lchild :
#                 self.lchild.insert(data)
                
#             else:
#                 self.lchild = BST(data)
#         else:
#             if self.rchild :
#                 self.rchild.insert(data)
                
#             else:
#                 self.rchild = BST(data)
                
#     def inorder(self):
#         if self.lchild:
#             self.lchild.inorder()
#         print(self.key, end=" ")
#         if self.rchild:
#             self.rchild.inorder()
            
#     def postorder(self):
#         if self.lchild:
#             self.lchild.postorder()
            
#         if self.rchild:
#             self.rchild.postorder()
#         print(self.key , end=" ")
        
#     def preorder(self):
#         print(self.key , end=" ")
#         if self.lchild:
#             self.lchild.preorder()
            
#         if self.rchild:
#             self.rchild.preorder()
        
          
# root = BST(50)

# root.insert(10)
# root.insert(20)
# root.insert(30)
# root.insert(80)
# root.insert(40)
# print("Inorder BST")
# root.inorder()
# print("\npostorder BST")
# root.postorder()
# print("\npreorder BST")
# root.preorder()


        


# class BST:
#     def __init__(self , key):
#         self.key = key
#         self.lchild = None
#         self.rchild = None
        
#     def insert(self , data):
#         if self.key is None:
#             return 
#         if self.key == data:
#             return 
#         if data < self.key:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = BST(data)
                
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = BST(data)
                
#     def search(self ,data):
#         if self.key == data:
#             print("Node is Found")
#             return 
#         if data < self.key:
#             if self.lchild:
#                 self.lchild.search(data)
#             else:
#                 print("Node is not present ")
#         else:
#             if self.rchild:
#                 self.rchild.search(data)
#             else:
#                 print("Node is not present")
            
        
#     def preorder(self):#NLR
#         print(self.key , end=" ")
#         if self.lchild:
#             self.lchild.preorder()
            
#         if self.rchild:
#             self.rchild.preorder()
            
            
#     def inorder(self):
#         if self.lchild:
#             self.lchild.inorder()
        
#         print(self.key , end=" ")
        
#         if self.rchild:
#             self.rchild.inorder()
            
#     def postorder(self):
#         if self.lchild:
#             self.lchild.postorder()
            
#         if self.rchild:
#             self.rchild.postorder()
#         print(self.key , end=" ") 
        
#     def delete(self , data):
#         if data < self.key:
#             if self.lchild:
#                 self.lchild = self.lchild.delete(data)
                
#         elif data > self.key:
#             if self.rchild:
#                 self.rchild = self.rchild.delete(data)
                
#         else:
#             if self.lchild is None:
#                 temp = self.rchild
#                 self = None
#                 return temp
                
#             if self.rchild is None:
#                 temp = self.lchild
#                 self = None
#                 return temp
                
#             node = self.rchild 
#             while node.lchild:
#                 node = node.lchild 
#             self.key = node.key
                
#             self.rchild = self.rchild.delete(node.key)
#         return self  
            
# root = BST(20)
# list1 = [22,4,34,32,56,7,44]
# for i in list1:
#     root.insert(i)
# root.preorder()
# print()
#root.search(22)
#root.delete(22)
#root.preorder()
  '''         
def new_func():
    def Element(arr):
        n = len(arr)
        ans = []* n 
        stack = []
    
        for i in range(n-1, -1,-1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1]
            stack.append(arr[i])
        
        return ans
    arr = [23,43,12,23]
    print("Input" , arr)
    print(Element(arr))

    return new_func()
  '''

