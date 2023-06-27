cars = 100 # number of cars
space_in_a_car = 4.0 # number of space per car
drivers = 30 #numbber of drivers
passengers = 90 #total passengers
cars_not_driven = cars - drivers #cars_not_driven = totalCars-totalDrivers
cars_driven = drivers #cars_driven  = how many drivers
carpool_capacity = cars_driven * space_in_a_car # carpool_capacity = cars_driven x space in a car
average_passengers_per_car = passengers / cars_driven
#average_passengers_per_car = totalPassenger/ cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers,"drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")



# study drill answer
# If you use 4 and not 4.0 in space_in_a_car, the result of future calculation is also a INT not a Float /
# 
#
