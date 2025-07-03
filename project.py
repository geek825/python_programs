import random

while True:
    user=int(input("Enter the Rock for 1, Pepar for 2, scissors for 3 "))
    
    if user==1:
        user_choice="Rock" 
        
    elif user==2:
        user_choice="Pepar"
    
    elif user==3:
        user_choice="scissor"   
        
    try :
        pass
    except Exception as e:
        print("You make a mistake")
        
    print("user choice :",user_choice)
    computer=random.randint(1,3)        #Get a random number
    
    if computer==1:
        computer_name="Rock"
    elif computer==2:
        computer_name="Pepar"
    elif computer==3:
        computer_name="Scissors"
        
    print("computer choice is : ",computer_name)
    if user==computer:
        result="draw"

    elif(user==1 and computer==2) or (computer==1 and user==2):
        result="Rock"
        
    elif(user==1 and computer==3)or (computer==3 and user==1):
        result="Pepar"
    
    elif (user==2 and computer==3) or (computer==2 and user==3):
        result="scissors"
        
    if result=="draw":
        print("draw the game")
        
    elif result==computer_name:
        print("Oohooo Your are win ")
        
    else:
        print("Oops your are lose Computer are win ")
      