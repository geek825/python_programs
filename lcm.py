def compute_lcm(x,y):
    if x>y:
        greter=x
    else:
        greter=y
    while(True):
        if((greter%x==0) and(greter%y==0)):
            lcm=greter
            break
        greter +=1
    return lcm 
num1=int(input("Enter the number :"))
num2=int(input("Enter the 2nd number :"))
print(compute_lcm(num1 , num2))   

        
          
           