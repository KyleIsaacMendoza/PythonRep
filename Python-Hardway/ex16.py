# Reading and Writing Files
# Other file functions
# read()
# readline() - read one line 
# truncate() - Empties the file
# write('stuff') - Write 'stuff' to the file.
# seek(0) - Moves the read/write location to the beginning of the file.

from sys import argv
# we will take a file name as argument
script, filename = argv


print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # target will open (filename, 'w')
# w - is for write mode, but there are other mode such as 'r' - read, and 'a' - append
# 'r' is the default of opening file.


print("Truncating the file. Goodbye!")
target.truncate() # This will Delete everthing inside the file.

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ") # 
line2 = input("Line 2: ") # 3 Lines that we will write inside the file
line3 = input("Line 3: ") #

print("I'm going to write these to the file.")

target.write(line1) # inserting what we write inside the file
target.write("\n") # inserting what we write inside the file
target.write(line2) # inserting what we write inside the file
target.write("\n") # inserting what we write inside the file
target.write(line3) # inserting what we write inside the file
target.write("\n") # inserting what we write inside the file


print("And finally, we close it.")
target.close() # closing it