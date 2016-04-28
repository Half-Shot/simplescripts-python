# Files

file = input("Give me a filename:")

f = open(file,'r') #r for read, think chmod

text = f.read() # Read all the text in one blob.

f.close() # Close the file after finishing

