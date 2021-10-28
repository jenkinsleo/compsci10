#simple program that calculates the sum of numbers in a range

#gets the 2 numbers

number_1 = int(input("Enter number 1?:"))
number_2 = int(input("Enter number 2?:"))


final_total = 0
final_response = ""

for number in range(number_1, number_2 + 1):
    final_total += number


    if number == number_1:
        final_response = f"{number}"
    else:
        final_response += f" + {number}"

#adds the final number add the the end of the string and prints
final_response += f" = {str(number)}"

print(final_response)
