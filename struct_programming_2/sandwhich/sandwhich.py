#less simple python programming that calculates the cost of a sandhwich based off of user input

#prices dict that contains all the prices

size = {"large":4, "small":2.5}
prices = {"cheese":0.50, "tomatoes":0.25, "lettuce":0.10, "onions":0.10,}

def get_order():
    final_order = {"toppings": []}
    #gets the user order and returns a dict with their choices

    size = str(input("Large or small (L or S): ")).upper()
    if size == "L":
        final_order["size"] = 'large'

    else:
        final_order['size'] = 'small'

    #gets the toppings and adds them to the toppings list of the response from user is yes

    cheese = str(input("Cheese (Y or N)?: ")).upper()
    if cheese == "Y":
        final_order['toppings'].append("cheese")

    tomatoes = str(input("Tomatoes (Y or N)?: ")).upper()
    if tomatoes == "Y":
        final_order['toppings'].append("tomatoes")

    lettuce = str(input("Lettuce (Y or N)?: ")).upper()
    if lettuce == "Y":
        final_order['toppings'].append("lettuce")

    onions = str(input("Onions (Y or N)?: ")).upper()
    if onions == "Y":
        final_order['toppings'].append("onions")

    #gets the bs condiments (doesnt affect the order at all but makes the user happy)
    input("Ketchup (Y or N)?: ")
    input("Mayonnaise (Y or N)?: ")
    input("Mustard (Y or N)?: ")

    #returns the order ready to be calculated
    return final_order

#calculates the total cost of the sandwhich
def calculate_cost(order):
    total_cost = 0

    #adds the size of sandwhich
    size_temp = order["size"]
    total_cost = total_cost + size[size_temp]

    #goes through every topping and adds the price
    for x in order["toppings"]:
        price_temp = prices[x]
        total_cost = total_cost + price_temp

    return total_cost


if __name__ == "__main__":
    print(f"The total cost is: ${calculate_cost(get_order())}")