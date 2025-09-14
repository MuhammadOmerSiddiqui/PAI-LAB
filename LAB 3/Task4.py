n = int(input("Enter the number of elements:"))
list1 = [] 
list2 = []
for i in range(0,n):
    value = input(f"Enter the {i+1} value of list 1:")
    list1.append(value)
for i in range(0,n):
    value = input(f"Enter the {i+1} value of list 2:")
    list2.append(value)
def make_dictionary(list1,list2,n):
    dictionary = {}
    for i in range(0,n):
        dictionary[list1[i]] = list2[i]
    with open("file.txt","w") as file:
        file.write(str(dictionary))
    return dictionary
dictionary = make_dictionary(list1,list2,n)
print(f"The dictionary is:{dictionary} and it has been stored in a file named file.txt")