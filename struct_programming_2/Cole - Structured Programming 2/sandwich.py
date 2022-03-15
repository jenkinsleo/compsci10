LARGE_PRICE = 4.0
SMALL_PRICE = 2.5
CHEESE_PRICE = 0.5
TOMATO_PRICE = 0.25
LETTUCE_PRICE = 0.10
ONIONS_PRICE = 0.10


#INPUT
size = input("What size of sandwich? (S or L)?:")
cheese = input("Would you like to add cheese (Y or N)?:")
tomatoes = input("Would you like to add tomatoes (Y or N)?:") 
lettuce = input("Would you like to add lettuce (Y or N)?:")
onions = input("Would you like to add onions (Y or N)?:") 
input("Would you like to add ketchup (Y or N)?:") 
input("Would you like to add mayonnaise (Y or N)?:")
input("Would you like to add mustard (Y or N)?:")

#PROCESS
if size.upper() == "L": 
    price =+ LARGE_PRICE
else: 
    price =+ SMALL_PRICE

if cheese.upper() == "Y":
    price += CHEESE_PRICE

if tomatoes.upper() == "Y":
    price += TOMATO_PRICE

if lettuce.upper() == "Y":
    price += LETTUCE_PRICE

if onions.upper() == "Y":
    price += ONIONS_PRICE

#Output
format_price = "{:.2f}".format(price)
print("Total price: $" + str(format_price))  