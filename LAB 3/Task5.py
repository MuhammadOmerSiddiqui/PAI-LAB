def palindrome_check(string):
    check = False 
    lower_string = string.lower()
    for i in range(0,len(lower_string)//2):
        if(lower_string[i]==lower_string[len(lower_string)-1-i]):
            check = True
        else: check = False
    if(check):
        print("String is a palindrome")
    else: print("String is not a palindrome")

string = input("Enter a string:")
palindrome_check(string)