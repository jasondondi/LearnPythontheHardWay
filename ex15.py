# import the argv module from sys
from sys import argv

# the arguments to python are "script", then "filename"
script, filename = argv

#the variable "txt" gets filled with whatever is in
#  filename.

txt = open(filename)

# filename came from the argv.
#  print txt. read makes it read.
print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
