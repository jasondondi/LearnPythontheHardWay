# imports argv and takes the commandline arguments to pass
from sys import argv

# arguments will be the script (program) and then filename
script, input_file = argv

# defines the function print_all, which will use the f.read() function
# to print the contents of the file.
def print_all(f):
    print(f.read())

# defines the rewind function, which just rebrands 'seek to 0'
def rewind(f):
    f.seek(0)

# prints a line, from wherever line_count is.
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += current_line
print_a_line(current_line, current_file)

current_line += current_line
print_a_line(current_line, current_file)

# What does the "f" do in the functions?
# The f is a variable, but this time it's a file.
# f reads the line and moves the "read head" to the next line.
