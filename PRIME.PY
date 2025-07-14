num=int(input("Enter the number"))

flag=False

if num==1 or num==0:
    flag=True
    
for i in range (2,num):
    if num%i==0:
        flag=True
        break
    
if flag:
    print(num,"This number is not a prime number")
else:
    print("This is a prime number",num)    