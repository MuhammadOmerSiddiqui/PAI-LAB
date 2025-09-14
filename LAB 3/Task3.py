def employee(name,salary=10000):
    tax = salary * 0.02
    salary = salary - tax
    print(f"The name of the employee is {name} and his salary after tax is {salary}")

employee("Omer",1000000)
employee("Kashif")