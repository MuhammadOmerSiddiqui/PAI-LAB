try:
    with open("sample.txt","r") as file:
        contents = file.read()
        word = input("Enter a word to find and replace from the file:")
        replace_word = input("Enter a word to replace:")
        if word in contents:
            contents = contents.replace(word,replace_word)
            print(contents)
            with open("sample.txt","w") as file:
                file.write(contents)
        else:
            print("Word does not exist in the file")
except FileNotFoundError:
    print("File not found")