import math as m
# def maths():
#     a=max(23,21,34,213,123)
#     b=min(22,33,45,32,51,2,4)
    
#     print("The maximum numbar is :",a)
#     print("The minimum number is :",b)
# maths()

# The math.ceil function are used for the rounding up of the number
# The math.floor functio are used fot the rounding down of the number 


# a=m.ceil(2.5)
# b=m.floor(3.5)
# print(a)
# print(b)


#The Fuction abs are used for return the postive number 
# x=abs(int(input("enter the number : ")))

# print(x)


# x=pow(3,4) # (3*3*3*3)
# print(x)

# base=int(input("Enter the base value :"))
# pow=int(input("Enter the power value :"))


# power=base**pow
# print(power)    

# digits=len(str(power))
# print(digits)

# while power>0:
#     modulo=power%10
#     print(modulo)
#     power = int((power - modulo)/10)
#     power=power//10 
#     print(power)


# n=0
# for i in range(1,1000):
#     if (i%3==0 )or(i%5==0):
#         print(i)
#         n+=i
# print(n)

def fibonanci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib=fibonanci(n-1)
        fib.append(fib[-1]+fib[-2])
        return fib
    
print(fibonanci(10))    