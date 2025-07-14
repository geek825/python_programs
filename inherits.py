class person():
    def __init__(self,fname,lname,year): 
        self.firstname=fname
        self.lastname=lname
        self.year=year
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(self,fname,lname)
        self.graduationyear=year
x=student("yash","shelar","2004")   
print(x.graduationyear)