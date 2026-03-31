def writefile():
    file = open("D:/PycharmProjects/PythonProject/Rays Project 3/one/hello.txt", "w")
    file.write("Hi\n")
    file.write("I am writing first time in IO\n")
    file.write("This is a python program\n")
    file.close()
    print("File successfully written")

writefile()

def readfile():
    file = open("D:/PycharmProjects/PythonProject/Rays Project 3/one/hello.txt", "r")
    text = file.read()
    print(text)
    file.close()

readfile()

