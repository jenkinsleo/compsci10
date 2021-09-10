#simple program to check if the package is supported or not
weight_limit = 27
size_limit = 0.1
#gets 4 inputs
weight = float(input("What is the weight: "))

length = float(input("What is the length: "))
width = float(input("What is the width: "))
height = float(input("What is the height: "))


#calculates the dimensions in cubic meters
dimension = (length / 100) * (width / 100) * (height / 100)

#creates the output
if weight > weight_limit and dimension > size_limit:
    response = "too large and heavy"
elif weight > weight_limit:
    response = "too heavy"
elif dimension > size_limit:
    response = "too large"
elif dimension <= size_limit and weight <= weight_limit:
    response = "accepted"

print(response)