# While loops
# : colon tells python to start a new block


i = 0
numbers = []

# loop while loop 0 - 5
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)  # ! append(value) NOT append[value]

    i = i + 1
    print("Numbers now: ", numbers)  # This will print in array form
    # like this -> Numbers now: [0, 1, ...]

    print(f"At the bottom i is {i}")

print("The Numbers: ")

# print all data in numbers list
for num in numbers:
    print(num)
