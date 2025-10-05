import json
n = int(input("Enter how many key value pairs will be there in the dictionary:"))
dictionary = {}
for i in range(0,n):
    key = input(f"Enter the {i+1} name:")
    value = int(input(f"Enter the {i+1} age:"))
    dictionary[key] = value
with open("file.json","w") as file:
    json.dump(dictionary,file)
try:
    with open("file.json","r") as file:
        max_age = 0
        max_age_person = "" 
        dictionary1 = json.load(file)
        for key , value in dictionary1.items():
            if(value>max_age):
                max_age = value
                max_age_person = key
        for key , value in dictionary1.items():
            if(value==max_age):
                print(key,max_age)
except FileNotFoundError:
    print("Cannot open file")