class Student():
    def __init__(self, name, subject, marks= None):
        if marks is None:
            marks = []
        self.name = name
        self.subject = subject
        self.marks = marks
    def search_name(self,name):
        if name == self.name:
            print("Student Found")
        else:
            print("Student Not Found")  
    def add_marks(self, marks):
        self.marks.append(marks)
    
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)
    def how_grade(self):
        avg = self.calculate_average()
        
        if avg >= 90 and avg <= 100:
            return "A+"
        
        elif avg >=80 and avg < 90:
            return "A"
        
        elif avg >=70 and avg < 80:
            return "B+"
        
        elif avg >=60 and avg < 70:
            return "B"
        
        elif avg >=50 and avg <60:
            return "C"
        elif avg >=40 and avg <50:
            return "D"
        
        else:
            return "F"
        
    def display_report(self):
        print(f"Student Name: {self.name}")
        print(f"Subject: {self.subject}")
        print("Marks:", self.marks)
        print("Average Marks:", self.calculate_average())
        print("Grade:", self.how_grade())

student1 = Student(input("Enter a student name : "), "Python,java", [40,50,60,50,70])


student1.display_report()
