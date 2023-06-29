from sys import argv
# we take filename as an argument 
script, filename = argv

# variable of our file name
txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read()) # Read the context of our filename

print("Type the filename again: ")
file_again = input("> ") # store anything you input

txt_again = open(file_again) # this will save what you input and check if the validity if the file existing or not.


print(txt_again.read()) #will read the context of filename you input