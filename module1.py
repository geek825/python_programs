class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__ (self ):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n =  self.head
            
            while n is not None:
                print(n.data , end=" --> ")
                n = n.next
            print("None")    
    def add_begain(self , data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node        

    def add_after(self,data,x):
        n =  self.head 
        while n is not None:
            if x == n.data:
                break
            n = n.next
        
        if n is None:
            print("Linked list is empty")

        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next =  new_node
                
    def add_end(self ,data):
        

li = Linkedlist()
li.add_begain(20)
li.add_begain(10)
li.add_after(100, 10)
li.display()