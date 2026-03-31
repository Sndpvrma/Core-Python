import shutil

source = "C:/Users/Sandeep/Pictures/Screenshots/Screenshot.png"
target = "C:/Users/Sandeep/Desktop/New folder/Screenshot01.png"

shutil.copyfile(source, target)

print(source + " has been copied to " + target)