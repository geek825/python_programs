class Calculator():
    
    def __init__(self,num1,num2,):
       self.num1=num1
       self.num2=num2
    def add(self):
        print(c1.num1,"+",c1.num2,"=",c1.num1+c1.num2)
    def sub(self):
        print(c1.num1,"-",c1.num2,"=",c1.num1-c1.num2)   
    def mul(self):
        print(c1.num1,"*",c1.num2,"=",c1.num1*c1.num2) 
    def divide(self):
             print(c1.num1,"/",c1.num2,"=",c1.num1/c1.num2)
        
c1=Calculator(int(input("Enter the First number  ")),int(input("Enter the Seonf number  ")))
print(c1.add())
print(c1.sub())
print(c1.mul())
print(c1.divide())
