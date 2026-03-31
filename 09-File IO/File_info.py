def fileinfo():
    fo = open("C:/Users/Sandeep/Desktop/New folder/key_to_file.txt", 'r')
    print("file Name", fo.name)
    print("file Mode", fo.mode)
    print("Isclosed", fo.closed)

    fo.close()

    print("After Closed", fo.closed)

fileinfo()