# Create a for loop that calculates the product of all integers
# from n to m.
# Refer to unit tests for examples

# INPUT:
#  lower_bound:  (n | n belong to the number system N)
#  upper_bound:  (m | m belong to the number system N; m > n)
# 
#
# OUTPUT:
#  product of all values within bounds.
#       output = n * (n + 1) * (n+2) ... * m

lower_bound = int(input("Lower: "))
upper_bound = int(input("Upper: "))

#make sure max is above 0
if upper_bound < lower_bound:
    print("INVALID")
    exit()

total_product = lower_bound
for x in range(lower_bound, upper_bound):
    total_product = total_product * (x + 1) 

print(total_product)