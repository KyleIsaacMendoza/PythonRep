class Flight(): 
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = [] #empty list
        
    def add_passenger(self, name_of_passenger):
        if not self.check_seats():
            return False
        else: 
            self.passengers.append(name_of_passenger)
            return True
        
    def check_seats(self):
        return self.capacity - len(self.passengers)
    

flight = Flight(5)

list_of_names = ["Kyle","Mendoza","Isaac","Arambulo","Magnus","Gotham"]

for name in list_of_names:
    if flight.add_passenger(name):
        print(f"{name} is added to Flight succesfully!")
    else:
        print(f"{name} is not added because flight is full.")