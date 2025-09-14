def calculate_area(length,width):
    return length*width 

length = int(input("Enter the length of the rectangle:"))
width = int(input("Enter the width of the rectangle:"))
while(length<0):
    print("Invalid length! Please enter again:")
    length = int(input("Enter the length of the rectangle:"))
while(width<0):
    print("Invalid width! Please enter again:")
    width = int(input("Enter the width of the rectangle:"))

area = calculate_area(length,width)
print(f"The are of the rectangle is:{area}")
