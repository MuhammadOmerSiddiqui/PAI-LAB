list = ['a','e','i','o','u']
def string_vowel_check(string):
    string.lower()
    if string[-1] in list:
        return True
    else: return False

string = input("Enter a string:")
vowel_check = string_vowel_check(string)
if(vowel_check):
    print("Last letter is a vowel")
else:
    print("Last letter is a consonant")