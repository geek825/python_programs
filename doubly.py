class link:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        node1=link(10)
        node2=link(20)
        node3=link(20)
        node4=link(20)
        node5=link(20)
        
        node1.next=node2
        node2.next=node3
        node3.next=node4
        node4.next=node5
        
        currentNode=node1

        while currentNode:
            print(currentNode.data,end="-->")
            currentNode=currentNode.next
        print("null")
        
