password = input("Create a Password:")
character_check = False
digit_check = False
scharacter_check = False
length_check = False
password.lower()
length = len(password)
if(length>=8): length_check = True
for character in password:
    if(character>="a" and character<="z"):
        character_check = True
    if(character>="0" and character<="9"):
        digit_check = True
    if(character=="@" or character=="#" or character=="$" or character=="%"):
        scharacter_check = True
if(character_check and digit_check and length_check and scharacter_check):
    print("Valid Password")
else:
    print("Invalid Password")
