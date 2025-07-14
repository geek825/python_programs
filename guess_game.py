import random
target=random.randint(1,100)

while True:
    guess=int(input("guess the number or quit:"))
    # if (guess =="Q"):
    #     break
    if(guess==target):
        print("success Your are right guess ")
        break
    elif (guess>target):
        print("you are guess the bigeer number,take a smaller number")
    else:
        print("you are guess the smaller number,take a bigger number")
    
print("___game over___")