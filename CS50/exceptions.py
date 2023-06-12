import sys #to import sys.exit(1) -> to exit program


try:
    x = int(input("X: "))
    y = int(input("Y: "))
except ValueError: 
    print("Error: Invalid Input")
    sys.exit(1)
    
    
#result computation
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Number divided by 0 is undefined")
    sys.exit(1)
    

print(f"{x} / {y} = {result}")
    