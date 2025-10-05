try:
    number1 = int(input("Enter a number:"))
    number2 = int(input("Enter any other number:"))
    result = number1/number2
    print(result)
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Number is not integer type")