#simple program to check if the package is supported or not
WEIGHT_LIMIT = 27
SIZE_LIMIT = 0.1
#gets 4 inputs
weight = float(input("What is the weight: "))

length = float(input("What is the length: "))
width = float(input("What is the width: "))
height = float(input("What is the height: "))


#calculates the dimensions in cubic meters
dimension = (length / 100) * (width / 100) * (height / 100)

#creates the output
if weight > WEIGHT_LIMIT and dimension > SIZE_LIMIT:
    response = "too heavy and too large"
elif weight > WEIGHT_LIMIT:
    response = "too heavy"
elif dimension > SIZE_LIMIT:
    response = "too large"
elif dimension <= SIZE_LIMIT and weight <= WEIGHT_LIMIT:
    response = "accepted"
else:
    response = "INVALID"

print(response)