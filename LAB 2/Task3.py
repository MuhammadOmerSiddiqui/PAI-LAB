# Sample list of student records (name, marks)
students = [
    ("Ali", 85),
    ("Sara", 92),
    ("Ahmed", 76),
    ("Fatima", 95),
    ("Omer", 88),
    ("Zain", 91)
]
print("List Before Sort:")
print(students)
for i in range(0,len(students)-1):
    for j in range(0,len(students)-1-i):
        if(students[j][1]<students[j+1][1]):
            temp = students[j]
            students[j] = students[j+1]
            students[j+1] = temp 
print("List After Sort:")
print(students)
print("Top 3 students:")
for i in range(0,3):
    print(students[i])