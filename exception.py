
#Value error example

# try:
#     name=int(input("enter the name ::"))
# except ValueError as e:
#     print("This is the error message value error")
# except Exception as e:  
#     print(e)
# print("thank you")

#ZeroDivisonError example 


# num=int(input("Enter the the first number :"))
# num2=int(input("Enter the 2nd number :"))

# try :
#     print(f"Divide {"num/num2"}",num/num2)
    
# except ZeroDivisionError as e:
#     print("Hello coder this is not divisible by zero try another number")
    
# except ValueError as e:
#     print("This Input is only accept a integer value")
    
# else:
#     print("Our code executed successfully")    

# finally:
#     print("Thank you")

#raised Exception example


def exception1():
    num=int(input("enter the numeber :"))

    if num>0:
        raise Exception("this is not a negetive number")
    else:
        print("this is a negetive number")
exception1()




