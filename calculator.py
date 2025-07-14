def add(x,y):
    return x+y

def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def divide(x,y):
    return x/y

print("select the method ")
print("1 Addition")
print("2 Substraction")
print("3 Multipication")
print("4 division")

while True: 
    choice=input("enter the choice")
    if choice in ('1','2','3','4'):
        try:
            num1=float(input("enter the first number"))
            num2=float(input("enter the second number"))
        except ValueError:
            print("Invalid input")
            continue
        if choice=='1':
            print(num1,"+",num2,"=", add(num1,num2))
            
        elif choice=='2':
            print(num1,"-",num2,"=", sub(num1,num2))
            
        elif choice =='3':
            print(num1,"*",num2,"=", mul(num1,num2))
            
        elif choice=='4':
            print(num1,"/",num2,"=", divide(num1,num2))
            
        else:
            print("invalid input")