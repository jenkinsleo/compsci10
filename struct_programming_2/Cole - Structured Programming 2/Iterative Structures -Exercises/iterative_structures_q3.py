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

value = int(input())
divisor = int(input())

n = 0

while value > 1:
    value = value / divisor
    n += 1

print(n)
