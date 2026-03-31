def readfile():
    file = open("D:/PycharmProjects/PythonProject/Rays Project 4/one/hello.txt","r")
    text = file.read()
    print(text)
    file.close()

readfile()

def writefile():
    file = open("C:/Users/Sandeep/Desktop/New folder/hello.txt","w")
    file.write("Hello World\n")
    file.write("this file was save on other place before\n")
    file.write("After this file is save here\n")
    file.close()
    print("File successfully written")

writefile()
