#3 functions that are for working with canadian currency

#gets amount of quarters, dimes, nickels and pennies and returns the total
def add_coins(quarters, dimes, nickels, pennies=0):
    total_value = 0

    total_value += 0.25 * quarters
    total_value += 0.10 * dimes
    total_value += 0.05 * nickels
    total_value += 0.01 * pennies

    return total_value

#takes a dollar value and returns the amount of coins
def make_change(dollar_value):
    supported_coins = {"quarter": 0.25, "dimes": 0.1, "nickel": 0.05, "penny": 0.01}

    #starts with the higher value coins then works down the the lower value by bringing over the remainder

    new_money = dollar_value
    final_coins = {}

    for key in supported_coins:
        #gets how many of the selected coins will fit and adds that to the new dict
        final_coins[key], remainder = divmod(new_money, supported_coins[key])

        #for debugging purposes will print step by step checking every coin
        #print(f"Testing if {supported_coins[key]} ({key}) goes into {new_money}, {final_coins[key]}")
        
        #rounds and adds to the variable to be checked again with the next lowest coin interval
        new_money = round(remainder, 2)

    return tuple(final_coins)

def to_string(quarters, dimes, nickels,pennies):
    return f"quarters:{quarters}; dimes:{dimes}; nickels:{nickels}; pennies:{pennies}"

def to_string_from_tuple(coins):
    return to_string(coins[0],coins[1],coins[2],coins[3])


