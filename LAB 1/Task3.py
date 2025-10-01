number = int(input("Enter a number:"))
encrypted_number = 0
while(number>0):
    digit = number % 10
    number = number // 10
    digit += 7
    digit = digit % 10
    encrypted_number = (encrypted_number*10) + digit
print(f"The encrypted number is {encrypted_number}")