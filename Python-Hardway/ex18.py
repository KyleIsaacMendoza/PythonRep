# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args #declaring variables to store arguments
    print(f"arg1: {arg1}, arg2: {arg2}")



# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    
    
#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")
    
    
# this one takes no argument
def print_none():
    print("I got nothin'. ")
    

# Using your Function
print_two("Zed", "Shaw") # (*args)
print_two_again("Zed", "Shaw") #(arg1,arg2)
print_one("First!") # (arg1)
print_none() # no argument

