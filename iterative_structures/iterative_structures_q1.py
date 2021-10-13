# Create a for loop that creates a string containing n
# occurences of the word 'Ni! '. Do not use multiplicaton!
# Refer to unit tests for examples

repeat_amount = int(input("Repeat: "))
repeated_string = ""

for repeat in range(0, repeat_amount):
    repeated_string = repeated_string + "Ni! "

print(repeated_string)
# INPUT:
#  repeat:  (n | n belong to the number system N)
#
# OUTPUT:
#  the string "Ni! " repeated n times

