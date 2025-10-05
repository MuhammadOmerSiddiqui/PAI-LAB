def function():
    sentence = input("Enter a question:")
    if("?" in sentence):
        with open("questions.txt","a") as file:
            file.write(sentence)
    else:
        print("This is not a question")

function()