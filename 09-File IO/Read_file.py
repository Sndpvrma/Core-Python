def readfile():
    file = open("D:/PycharmProjects/PythonProject/Rays Project 4/one/hello.txt", "r")
    text = file.read()
    print(text)
    file.close()

readfile()