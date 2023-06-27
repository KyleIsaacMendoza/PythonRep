# Strings asnd Text

# .format()

types_of_people = 10 # variable that stores the number of people
x = f"Ther are {types_of_people} types of people."

# variable that stores tha string "binary" and don't
binary = "binary"
do_not =  "don't"

# variables that the values is = to string that uses variale binary & do_not
y = f"Those who know {binary} and those who {do_not}"

#print x and y
print(x)
print(y)

#Print x and y
print(f"I said: {x}")
print(f"I also said: {y}")

# hilarious stores boolean
hilarious = False
joke_evaluation = "Isn't that so funny?! {}" # leave curly braces for .format(parameter) 

# uses .format
print(joke_evaluation.format(hilarious))


w = "This is the left side of..."
e = "a string with a right side."


# concat string using + 
print( w + e)