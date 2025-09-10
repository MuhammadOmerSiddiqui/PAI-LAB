student_dictionary = {}
def add_student(name,marks):
    student_dictionary.update({name:marks})
    # student_dictionary[name] = marks (Both lines are equivalent)

def view_records():
    print(student_dictionary)

def update_marks(name,marks):
    if name in student_dictionary:
        student_dictionary[name] = marks
        print("Marks Updated Successfully")
    else:
        print("Student does not exist")

def delete_student(name):
    if name in student_dictionary:
        del student_dictionary[name]
        print("Student Removed Successfully")
    else:
        print("Student does not exist")

def topper():
    max_marks = max(student_dictionary.values())
    for name , marks in student_dictionary.items():
        if(marks==max_marks):
            return name

print("-"*5,"Welcome To Student Management System","-"*5)
print("1.Add a student")
print("2.Update Student's Marks")
print("3.Remove a student")
print("4.Find the topper")
print("5.View Records")
print("6.exit")
choice = int(input("Enter your choice:"))
while(choice!=6):
    if(choice==1):
        name = input("Enter student's name:")
        marks = int(input("Enter student's marks:"))
        add_student(name,marks)
        print("Student Added Successfully")
        print("1.Add a student")
        print("2.Update Student's Marks")
        print("3.Remove a student")
        print("4.Find the topper")
        print("5.View Records")
        print("6.exit")
        choice = int(input("Enter your choice:"))
    elif(choice==2):
        name = input("Enter student's name whose marks you want to update:")
        marks = int(input("Enter this student's updated marks:"))
        update_marks(name,marks)
        print("1.Add a student")
        print("2.Update Student's Marks")
        print("3.Remove a student")
        print("4.Find the topper")
        print("5.View Records")
        print("6.exit")
        choice = int(input("Enter your choice:"))
    elif(choice==3):
        name = input("Enter student's name which you want to remove:")
        delete_student(name)
        print("1.Add a student")
        print("2.Update Student's Marks")
        print("3.Remove a student")
        print("4.Find the topper")
        print("5.View Records")
        print("6.exit")
        choice = int(input("Enter your choice:"))
    elif(choice==4):
        print(f"The topper is {topper()} and his marks are {student_dictionary[topper()]}")
        print("1.Add a student")
        print("2.Update Student's Marks")
        print("3.Remove a student")
        print("4.Find the topper")
        print("5.View Records")
        print("6.exit")
        choice = int(input("Enter your choice:"))
    elif(choice==5):
        view_records()
        print("1.Add a student")
        print("2.Update Student's Marks")
        print("3.Remove a student")
        print("4.Find the topper")
        print("5.View Records")
        print("6.exit")
        choice = int(input("Enter your choice:"))
print("Program Terminated")