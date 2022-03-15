#CONSTANTS
WEIGHT_LIMIT = 27
VOLUME_LIMIT = 0.1

#Input
weight = float(input("Weight in kilograms? "))
length = float(input("Length? "))
width = float(input("Width? "))
height = float(input("Height? "))

#Process
length = length / 100
width = width / 100
height = height / 100

volume_of_package = length * width * height
volume_of_package = round(volume_of_package, 3)

if weight <= WEIGHT_LIMIT and volume_of_package <= VOLUME_LIMIT:
    output = "accepted"
elif weight > WEIGHT_LIMIT and volume_of_package > VOLUME_LIMIT:
    output = "too heavy and too large"
elif weight > WEIGHT_LIMIT:
    output = "too heavy"
elif volume_of_package > VOLUME_LIMIT:
    output = "too large"
else:
    output = "Error"

#Output
print(output)
