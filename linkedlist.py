# linkedlist without class

# node1={'data': '10', 'next': None}
# node2 = {'data' : '20', 'next': None}
# node3 = {'data' : '30' , 'next' : None }
# node4 = {'data' : '30' , 'next' : None}


# node1['next'] = node2
# node2['next'] = node3
# node3['next'] = node4
# node4['next'] = None

# currentnode = node1
# while currentnode is not None:
#     print(currentnode['data'] , end=" ---> ")
#     currentnode = currentnode['next']
# print(None)


# linkedlist using class
# class Linkedlist:
#     def __init__(self,data):
#         self.data  = data
#         self.next = None
        
# node1 = Linkedlist(10)
# node2 = Linkedlist(20)    
# node3 = Linkedlist(30)
# node4 = Linkedlist(40)
    
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = None
    
# currentnode = node1
# while currentnode.next:
#     print(currentnode.data,end=" --> ")
#     currentnode = currentnode.next
# print(None)


class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
class Linklist :
    def __init__(self):
        self.head = None
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
            
        else:
            n =  self.head
            while n is not None:
                print(n.data, end=" ---> ")
                n = n.next
    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def add_end(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head 
            while n.next is not None:
                n = n.next
            n.next = new_node
             
             
    def add_after(self , data,x):
        n=self.head
        
        while n is not None:
            if x==n.data:
                n = n.next
            if n is None:
                print("Linkedlist is empty")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node
                
            
li = Linklist()
li.add_begin(10)
li.add_begin(20)
li.add_after(100,20)
li.display()
