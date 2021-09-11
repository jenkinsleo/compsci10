# Create a for loop that creates a string containing n
# occurences of the word 'Ni! '. Do not use multiplicaton!
# Refer to unit tests for examples

n = int(input("Repeat: "))
repeated_string = ""

for x in n:
    repeated_string = repeated_string + "Ni! "

print(repeated_string)
# INPUT:
#  repeat:  (n | n belong to the number system N)
#
# OUTPUT:
#  the string "Ni! " repeated n times

