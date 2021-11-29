password_md5 = 'a1d0c6e83f027327d8461063f4ac58a6'

import hashlib

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

count = 0
run = True
while run:
    pw = hashlib.md5(input("Password: ").encode())
    pw = pw.hexdigest()

    if pw == password_md5:
        print("You may pass")
        run = False
    else:
        count = count + 1
        if count == 3:
            print("Entry denied")
            run = False
        if run == True:

            print("Try again")



    