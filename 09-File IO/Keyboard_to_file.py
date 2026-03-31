def keyboard_to_file():
    file = open("C:/Users/Sandeep/Desktop/New folder/key_to_file.txt","w")
    text = input("Enter your text here: ")

    while (text != "Stop"):
        file.write(text)
        file.write(" ")
        file.write("\n")
        text = input('')

    file.close()

keyboard_to_file()
