class Student(): #class
    college="HV Desai college"
    name="prinjal"
    def __init__(self,fullname,age,markes): #constructor
        self.name= fullname
        self.age=age
        self.marks=markes
      
    def display(self):        #method
        print("hello",self.name)
s1=Student("yash","20","66") 
s1.display()
print(s1.name,s1.age,s1.marks)


