class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    #static method 
    @staticmethod
    def hello():
        print("hello")
        
    def get_avg(self):
            sum=0
            for val in self.marks:   
                sum+=val
                print("hello",self.name,"Your score is in  ",sum/3)
                      
   
s1= Student("yash", [90,49,86])                  
s1.get_avg()
        