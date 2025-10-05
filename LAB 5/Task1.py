with open("file.txt","w") as file:
    file.write("I love python!!!\n")
    file.write("I love C++!!!\n")
    file.write("I love AI!!!")
try:
    with open("file.txt","r") as file:
        count = 0 
        count2 = 0
        contents = file.readlines()
        for line in contents:
            word = line.split()
            count += len(word)
            for character in line:
                if(character!="" and character!="\n"):
                    count2 += 1
        print(f"The number of characters in the file are {count2}")
        print(f"The number of words in the file are {count}")
except FileNotFoundError:
    print("File not found")
