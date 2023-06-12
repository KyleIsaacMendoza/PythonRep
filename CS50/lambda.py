people = [
    {"name" : "Kyle", "address": "1722 Santiago St.", "city": "Manila"},
    {"name": "Isaac", "address": "1276 San Nicolas St.", "city": "Quezon"}
]

people.sort(key = lambda address: address["address"])

print(people)