#Constants
ADULT_PRICE = float(12.50)
CHILD_PRICE = float(8.25)
SENIOR_DISCOUNT_AS_DECIMAL = 0.75
SENIOR_PRICE = float(ADULT_PRICE * SENIOR_DISCOUNT_AS_DECIMAL)

#Input
movie_name = input("Movie?:")
adult_amount = int(input("Adults?:"))
child_amount = int(input("Children?:"))
senior_amount = int(input("Seniors?:"))

#This calculates the total price of each age group
adult_total = adult_amount * ADULT_PRICE
child_total = child_amount * CHILD_PRICE
senior_total = senior_amount * SENIOR_PRICE
total_price = float(adult_total + child_total + senior_total)

#This is so the price is set in dollars
total_price = round(total_price, 2)
format_total_price = "{:.2f}".format(total_price)

#This is the formating process
print('-' * 30)
print("|" + "{:^28}".format("*** " + movie_name + " ***") + "|")
print("| " + '{:13}'.format("Adults:") + "{:>13}".format(adult_amount) + " |")
print("| " + '{:13}'.format("Children:") + "{:>13}".format (child_amount) + " |")
print("| " + '{:13}'.format("Seniors:") + "{:>13}".format (senior_amount) + " |")
print("| " + '{:16}'.format("Total:") + "{:>4}".format (str("$ ")) + "{:>6}".format (format_total_price) + " |")
print('-' * 30)
