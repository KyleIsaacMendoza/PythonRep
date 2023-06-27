#import 
# this is how you add modules/features/libraries
# from sys module import argv
# argv -> is the argument variable, standard name in programming
#read the WYSS section for how to run this

from sys import argv 

script, first, second, third = argv


print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


# study drills #3 combiine input with argv

print("Input another argument: ")
argv = input()

# to run 
# command shell
# python ex13.py arg1, arg2, arg3

