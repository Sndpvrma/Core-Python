import re
import os

def readline():
    input_file = open('C:/Users/Sandeep/Desktop/New folder/Mail_file.txt', 'r')
    output_file = open('C:/Users/Sandeep/Desktop/New folder/Filtered_mail.txt', 'w')


    for line in input_file:
        if (re.search("@gmail.com", line)):
            output_file.write(line)

    input_file.close()
    output_file.close()

readline()