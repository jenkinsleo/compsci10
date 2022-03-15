QUARTER = 0.25
DIME = 0.1
NICKEL = 0.05
PENNY = 0.01


def add_coins(quarters=0, dimes=0, nickels=0, pennies=0):
    total = 0
    total += quarters * QUARTER
    total += dimes * DIME
    total += nickels * NICKEL
    total += pennies * PENNY
        
    return total
        
def make_change(dollar_value):
   coin_dict = {"quarters": QUARTER, "dimes": DIME, "nickels": NICKEL, "pennies": PENNY}

   final_dict = {}
   for coin in coin_dict:
       remainder, dollar_amount = (divmod(dollar_value, coin_dict[coin]))
       remainder = round(remainder, 10)
       dollar_value = round(dollar_amount, 10)
       final_dict[coin] = round(remainder)

   coins = (final_dict["quarters"], final_dict["dimes"], final_dict["nickels"], final_dict["pennies"])

   return coins


def to_string(quarters, dimes, nickels, pennies):
   final_dictionary = {"quarters": quarters, "dimes": dimes, "nickels": nickels, "pennies": pennies}

   final_string = ("quarters:" + str(final_dictionary["quarters"]) + "; " + "dimes:" + str(final_dictionary["dimes"]) + "; " + "nickels:" + str(final_dictionary["nickels"]) + "; " + "pennies:" + str(final_dictionary["pennies"]))

   return final_string
    
def to_string_from_tuple(coins=0):
    quarters = coins[0]
    dimes = coins[1]
    nickels = coins[2]
    pennies = coins[3]

    return to_string(quarters, dimes, nickels, pennies)