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


lower_bound = int(input())
upper__bound = int(input())

n = lower_bound
output = n

for _ in range(lower_bound, upper__bound):
    n += 1
    output = output * n

print(output)
