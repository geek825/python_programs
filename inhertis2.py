class employee:
    def __init__(self,name,age,salary):
        self.fullname=name
        self.age=age
        self.salary=salary

        def printname(self,fullname,age,salary):
            print(self.fullname,self.age,self,salary)
         
class manager(employee):
 def __init__(self,name,age,salary):
    super().__init__(self,age,salary)
    self.empname=name 
x=manager("yash","20","30000")  
print(x.empname,x.age,x.salary)