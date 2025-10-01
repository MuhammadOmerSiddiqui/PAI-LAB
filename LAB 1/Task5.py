list = ["@","#","%","&","*"]
name = input("Enter your name:")
birth_year = input("Enter your birth year:")
password = name[0:3] + birth_year[2:len(birth_year)] + list[ord(name[0])%5]
print(f"Generated Password is {password}")