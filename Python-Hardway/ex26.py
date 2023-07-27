# Dictionaries, oh lovely Dictionaries

# create a mapping of state to abbreviation


states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}


# Create a basic set of states and some cities in them

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}


# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'


# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])


# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])


# Do it by using the state then cities dictionary
print("-" * 10)
print("Michigan has: ", cities[states['Michigan']])
# cities key = the value of states['michigan'] which represent another value in CITIES dictionary in this case 'detroit'
print("Florida has: ", cities[states['Florida']])


# Print every state abbreviation
print('-' * 10)
#   key , value in list(dictionaries.items()) -> syntax
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")


# Print every cities abbreviation
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")


# now do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")


# safely got a abbreviation by state that might now be there
print("-" * 10)
# .get('key') -> get() will check if there is existing value without giving an error.
state = states.get('Texas')
if not state:
    print("Sorry, to Texas.")


# get a city with a default value (of error message)

city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")
