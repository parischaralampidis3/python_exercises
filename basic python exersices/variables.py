#variables and names 

#this is a variable that sets an integer value to 100
cars = 100

#this is a variable that sets a  float value to 4.0 
space_in_a_car = 4.0

passengers =90
#this is a variable that sets an intenger value of passengers to 30
drivers = 30

#this ia a variable that makes a calculation, of the cars that are not driven. So it substracts the vaeiable of cars from drivers
cars_not_driven = cars - drivers

#this variable  re assigns variable drivers to cars_driven variable
cars_driven = drivers 


#this variable that is called the carpool_capacity, as it multiplies cars_driven to space_in_a_car 
carpool_capacity = cars_driven * space_in_a_car

#this variable counts the available number of passengers per car 
average_passengers_per_car = passengers // cars_driven

print ("There are ", cars, "cars available.")
print ("Thera are only ", drivers, "drivers available.")
print ("They will be ", cars_not_driven, "empty cars today.")
print ("We can transport ", carpool_capacity, "people today.")
print ("We have ", passengers, "to carpool today")
print("We need to put about ", average_passengers_per_car, "in each car.")
