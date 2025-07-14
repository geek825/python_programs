students = []
def add_student():
    student = {}
    student['name'] = input("Name: ")
    student['id'] = int(input("ID: "))
    student['class'] = input("Class: ")
    student['marks'] = float(input("Marks:"))
    students.append(student)

def display():
    print("Students Recorde")
    for student in students:
        print("The name of student is " ,   student.get('name'))
        print("The id of student is " , student.get('id'))
        print("The class student is " , student.get('class'))
        print("The marks of student is " , student.get('marks'))
    
def search_student():
    if not students:
        print("data are not present")
        return 
    search_id = int(input("Enter the id :"))
    found = False
    for student in students:
        if student.get('id') == search_id:
            print("\n Student found")
            print("The name of student is " ,   student.get('name'))
            print("The id of student is " , student.get('id'))
            print("The class student is " , student.get('class'))
            print("The marks of student is " , student.get('marks'))
            print(" ")
            found = True 
            break
    if not found :
        print("search id are not found")
def update():
    if not students:
        print("student information are not present")
        return 
    update_id = int(input("Enter the updated id"))
    for student in students:
        if student['id'] == update_id:
            print("Student are found enter the new information")
            student['name'] = input("Enter the name")
            student['id'] = int(input("Enter the id"))
            student['class'] = int(input("Enter the class"))
            student['marks'] = float(input("Enter the marks"))
            print("Student information update successfully...")
            
    print("Student are not found ")
def menu():
    
    while True:
        print("*** STUDENT MANAGMENT SYSTEM ***\n")
        print("1 for Add the student\n")
        print("2 display the student\n")
        print("3 search the student\n")
        print("4 update the information of student\n")
        print("5 Exit\n")
        
        choice  = input("Enter choice 1/2/3/4/5 ")
        print("-" * 74)
        if choice == '1':
            add_student()
        elif choice == '2':
            display()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update()
        elif choice == '5':
            print("Exciting....")
            break
        
        else:
            print("Enter valid input")
menu()