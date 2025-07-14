class Employee:
    def __init__(self,Ename,Eid,Esal,Eroll):
        self.Ename=Ename 
        self.Eid=Eid
        self.Esal=Esal
        self.Eroll=Eroll
e1 = Employee ("Yash",23,20000,"Intern")
print("This is the Employe Name",e1.Ename)
print("This is the Employe id",e1.Eid)
print("This is the Employe salary",e1.Esal)
print("This is the Employe",e1.Eroll)
    
