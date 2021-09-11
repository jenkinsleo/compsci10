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

n = int(input("Lower: "))
m = int(input("Upper: "))

#make sure max is above 0
if m < n:
    print("INVALID")
    exit()

number = n
for x in range(n, m):
    number = number * (x + 1) 

print(number)