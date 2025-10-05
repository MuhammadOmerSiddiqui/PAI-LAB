with open("file3.txt","w") as file:
    name = input("Enter your name:")
    cnic_number = input("Enter your cnic number:")
    age = input("Enter your age:")
    salary = input("Enter your salary:")
    file.write("Name:" + name + "\n")
    file.write("Cnic Number:" + cnic_number + "\n")
    file.write("Age:" + age + "\n")
    file.write("Salary:" + salary + "\n")    
with open("file3.txt","a") as file:
    contact_number = input("Enter your contact number:")
    file.write("Contact Number:" + contact_number + "\n")
try:    
    with open("file3.txt","r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("File not found or cannot open file")