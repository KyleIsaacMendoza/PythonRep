# More files
# Write Python script to copy one file to another.


from sys import argv
from os.path import exists 
# exists will return a boolean weather the file existing or not. 

# save files to argv
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")


# We could do these two on one line, how?
in_file = open(from_file) # File with Data
indata = in_file.read() # saving the data using file.read()


print(f"The input file is {len(indata)} bytes long.") 
#checking what is the length of the data. Optional
 
print(f"Does the output file exist? {exists(to_file)}") 
# using the exists that we import to check if new file is existing. 

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w') #setting the new file to write mode
out_file.write(indata) 
# writing the file with the data saved inside indata

print("Alright, all done.")

out_file.close() # closing both files
in_file.close() # closing both files
# we close files to avoid some hard-to-debug issues 
# running out of files handles or corrupted data.


# to run 
# python ex17.py file_with_data.txt new_file.txt 