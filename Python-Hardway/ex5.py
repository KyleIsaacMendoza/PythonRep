# More variales and Printing

# format string -> must start print with 'f' for format
# use a special sequence to put variable inside them {variable}

# overall print(f"{somevar}")

name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")


# This line is tricky, try to get it exactly right 

total = age + height + weight
print(f"If i add {age}, {height}, and {weight} I get {total}.")


centimeters = height * 2.54
kilogram = weight * 0.453592


print(f"Height in Centimeters is {centimeters}")
print(f"Weight in Kilogram is {kilogram}")