# def Factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*Factorial(n-1)
# num=int(input("enter num : "))
# print(Factorial(num))



# def num(n):
#     if n==0:
#         return 
#     num(n-1)
#     print(n)
    
# num(5)


#sum of the number 1 To n

def sum(n):
    if n==1:
        return 1
    ans=n+sum(n-1)
    return ans

print(sum(6))



    
  
    
