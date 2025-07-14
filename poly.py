
#Polymorphism Program

class Vehical:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
        
    class car:
        def __init__(self,model,brand): 
            self.model=model
            self.brand=brand

        def move(self):
            print("Driving a car")
            
    class bike:
        def __init__(self,model,brand):
            self.model=model
            self.brand=brand
            
        def move(self):
            print("riding a bike")
    
    class bus:
        def __init__(self,model,brand):
            self.model=model
            self.brand=brand

        def move(self):
            print("Driving a bus")
            
car1=Vehical.car("swift","maruti")
bike1=Vehical.bike("pulsar","Hero")
bus1=Vehical.bus("Pmpml","Tata")

for x in (car1,bike1,bus1):
    x.move()
    