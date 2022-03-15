# Create a validation loop that asks the user for a password. They have three
# attempts to get the password correct. Otherwise, entry is denied.
# Refer to unit tests for examples

# INPUT:
#  password: alpha-numeric
#
#
# OUTPUT:
#   "You may pass" if password is 42
#   "Try again" in all other cases; password is reprompted
#   "Entry denied" and end of program if password is incorrect 3 times
#

# Example:
##
##    What is the password?:42
##    You may pass
##
##    What is the password?:41
##    Try again
##    What is the password?:42
##    You may pass
##
##    What is the password?:41
##    Try again
##    What is the password?:43
##    Try again
##    What is the password?:43
##    Entry denied
c = 0

while True:
    password = int(input(''))
    if password == 42:
        output = "You may pass"
        break
    else:
        c += 1
        if c < 3:
            print("Try Again")
        else:
            output = "Entry denied"
            break

print(output)
