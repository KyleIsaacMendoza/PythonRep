list_of_names = [
    "Harry",
    "Kyle",
    "Isaac"
]
print(list_of_names)

#append = add another value to the list
list_of_names.append("Mendoza")

for name in list_of_names:
    print(f"{name} sucessfully printed")
    

#Tuple - couple of values that aren't going to change

#instead of 
coordinateX = 10
coordinateY = 20

#you can do
coordinate = (10,20)
print(coordinate)

#creating set and add values
s = set()

s.add(1)
s.add(2)
print(s)


#dict - key & value pairs
person = {
    "name_student" : "gole",
    "section" : "engineer",
    "age" :18
}
print(person)

students = [
    {"names": "kyle", "section": "bsit"},
    {"names": "isaac", "section": "com-sci"}
]



print(students[0])