# Create a for loop that creates a string containing n
# occurences of the word 'Ni! '. Do not use multiplicaton!
# Refer to unit tests for examples


# INPUT:
#  repeat:  (n | n belong to the number system N)
#
# OUTPUT:
#  the string "Ni! " repeated n times

n = int(input())
output = ''

for _ in range(n):
    output += 'Ni! '

print(output)
