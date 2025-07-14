class Microsoft():
    def __init__(self,name,role,age,salary):
        try:
            if name==str:
                pass
        except TypeError as a :
            print("oops! This is the error message" )
            
        self.name=name 
        self.role=role
        self.age=age
        self.salary=salary
    
        def print(self,name,role,age,salary):
            print(self.name,self.role,self.age,self.salary)
class Employee(Microsoft):
    def __init__ (self,name,role,age,salary):
        super().__init__(name,role,age,salary)   
        self.employeerole=role
    # if __name__=="__main__":
    #     raise Exception ("Accepted")  
    
x=Microsoft("1234","intern","21","20000")
print(x.name,x.role,x.age,x.salary)
s1=Employee("mahesh","software developer","27","70000")
print("\n name =",s1.name,"\n role =",s1.role,"\n age =",s1.age," \n salary =",s1.salary)
s2=Employee("suresh","Project Manager","24","35000")
print("\n name =",s2.name,"\n role =",s2.role,"\n age =",s2.age," \n salary =",s2.salary)
s3=Employee("ravet shaha","Content Manager","26","50000")
print("\n name =",s3.name,"\n role =",s3.role,"\n age =",s3.age," \n salary =",s3.salary)
