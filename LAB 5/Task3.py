n = int(input("Enter the number of elements in the lists:"))
list1 = []
list2 = []
dictionary = {}
for i in range(0,n):
    element1 = input(f"Enter the {i+1} value for 1 list:")
    list1.append(element1)
    element2 = input(f"Enter the {i+1} value for 2 list:")
    list2.append(element2)
for i in range(0,n):
    dictionary[list1[i]] = list2[i]
with open("file2.txt","w") as file:
    file.write(str(dictionary))