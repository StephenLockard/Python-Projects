
garage = list()

for i in range(0, 6):
    garage.append(input("Adding the car to the garage:"))
vehicle = input("Which car in the garage do you want to be able to retrieve?")
counter = 0
while garage.pop() != vehicle:
    counter += 1
estimate = (counter+1) * 6
print(estimate, "minutes until your vehicle is ready")
