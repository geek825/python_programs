# num=int(input("Enter the number :"))
# num_squrt=num*num
# print((num_squrt))

n = int(input("Enter the number "))
while n>=1 and n<=20:
    if n%2!=0:
        print("Weird")
    elif n%2==0 and n>=2 and n<=5:
        print("Not Weird")
    
    elif n>=6 and n<=20:
        print("Weird")
    else:
        print("Not Weird")
print("Your are out of the range")