# Create a while loop that calculates the of times that start can be divided
# by divisor before it is less than or equal to one.
# Note that you are to use floating point division
# Refer to unit tests for examples

# INPUT:
#  value:   (v | v belong to the number system N)
#  divisor: (d | n belong to the number system N)
#
# OUTPUT:
#  number of divisions: (n | n belong to the number system N)     

value = float(input("Value: "))
divisor = float(input("Divisor: "))

number_divisions = 0
while True:
    number_divisions =  number_divisions + 1
    if value <= divisor:
        break

    value = value // divisor

print(number_divisions)