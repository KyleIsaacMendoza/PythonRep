# Function and Files


from sys import argv

script, input_file = argv  # You will input argv in running this file
# example python ex20.py file_name.txt

# Function to print everthing inside the file


def print_all(f):
    print(f.read())

# Function to set the line into start


def rewind(f):
    f.seek(0)


# Function to print certain number of lines
def print_a_line(line_count, f):
    print(line_count, f.readline())


#
current_file = open(input_file)  # declare variable for file argument


print("First let's print the whole file: \n")
# call the function that print the whole file
print_all(current_file)

# Now let's rewind, kind of like a tape.
# call the function rewind(file)
# you need to rewind first before you use print a line to move the file at the starting point.
rewind(current_file)


# Print the three Lines
print("Let's print Three lines: ")

# Line to print
current_line = 1
# call function that print certain line in a file in this case
# Function print_a_line
print_a_line(current_line, current_file)


current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
