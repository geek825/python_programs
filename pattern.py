# rows=5

# for i in range(rows):
#     for j in range(i+1):
#         print("* ", end="")

#     print()
#     rows=5

# for i in range(rows):
#     for j in range(i+1):
#         print("* ", end="")

#     print()
    
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import queue
queue=[]
def enqueue():
    elements=int(input("Enter the elements"))
    e1=queue.append(elements)
    print("added elements",)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop()
        print("removed the element from the queue :",e)
def display():
   print(queue)
while True:
    choice=int(input("Enter the choice"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
        break
    else:
        print("Please enter the valid number")


        
        
        
    
    


        
        
        