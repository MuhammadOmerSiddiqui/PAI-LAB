def fix_file_text(file_name):
    try:
        with open(file_name,"r") as file:
            text = file.read()
        if "Thas" in text:
            corrected_text = text.replace("Thas","This",1)
        else:
            corrected_text = text
        with open(file_name,"w") as file:
            file.write(corrected_text)
        return corrected_text
    except FileNotFoundError:
        return "Error: File not found."
result = fix_file_text("replacement_needed.txt")
print(result)