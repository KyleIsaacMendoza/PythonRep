# Functions and Variables

#creating function with accept an argument of how any cheese and box of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
    

# calling function and passing 20 30 as value
print("We can just give the function numbers directly")
cheese_and_crackers(20,30)

# Calling function but using variables instead of straight values 
print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50


cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Calling function passing operation instead of variables or literals
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combite the two, variables and math:")

# Calling function using both literals and variables 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# Create another function
# Formula = (Base x Height) / 2
def area_of_triangle(base, height):
    print(f"The base is: {base} and height is: {height}")
    print(f"To find the area of a Tringle the Formula is (Base x Height) / 2")
    print(f"The area of a Triangle with a Base: {base}  and a Height: {height} is {(base*height)/2}")
    print("Well Done!\n")
    
    
base = float(input("Base: "))
height = float(input("Height: "))

area_of_triangle(base, height) 
area_of_triangle(10,20) # 2