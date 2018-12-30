# initializes the argv which accepts execution arguments
from sys import argv

# tells the program that the execution argument goes in the "filename" var
script, filename = argv

# the variable txt will be filled with the contents of the file
# filename is filled with the name of the file from the execution arg
# and this fills the txt variable with that.
txt = open(filename)

# %r gets filled with 'filename' and prints the line
print "Here's your file %r:" % filename
# txt is the contents of the file. read... uh... reads the variable contents?
print txt.read()

# displays a string that will be used as the promprt for user input
print "Type the filename again:"
# ask for raw_input and put the result in file_again
file_again = raw_input(">" )

# now we take the file_again input from the prompt
# and open the file into the txt_again variable
txt_again = open(file_again)

# and now we push txt.again to the read() function
print txt_again.read()
