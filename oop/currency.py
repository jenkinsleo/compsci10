#currency object file
#import this from another script
#made by yours truly
COIN_VALUE = {"quarter": 0.25, "dimes": 0.1, "nickel": 0.05, "penny": 0.01}



#idk does some stuff I just dont want to not comment what this does
def add_coins(quarters, dimes,nickels,pennies=0):
    final_value_in_dollars = 0

    final_value_in_dollars += quarters * COIN_VALUE['quarter']
    final_value_in_dollars += dimes * COIN_VALUE['dimes']
    final_value_in_dollars += nickels * COIN_VALUE['nickel']
    final_value_in_dollars += pennies * COIN_VALUE['penny']
    
    
    return final_value_in_dollars

#makes change thisfrom the other assignment
def make_change(dollar_value):
    #starts with the higher value coins then works down the the lower value by bringing over the remainder

    new_money = dollar_value
    final_coins = {}

    for key in COIN_VALUE:
        #gets how many of the selected coins will fit and adds that to the new dict
        final_coins[key], remainder = divmod(new_money, COIN_VALUE[key])

        #for debugging purposes will print step by step checking every coin
        #print(f"Testing if {supported_coins[key]} ({key}) goes into {new_money}, {final_coins[key]}")
        
        #rounds and adds to the variable to be checked again with the next lowest coin interval
        new_money = round(remainder, 2)

    return (int(final_coins['quarter']),int(final_coins['dimes']),int(final_coins['nickel']),int(final_coins['penny']))

#makes string from a tuple
def to_string_from_tuple(money_list):
    return f'quarters:{int(money_list[0])}; dimes:{int(money_list[1])}; nickels:{int(money_list[2])}; pennies:{int(money_list[3])}'

#makes a string not from a tuple
def to_string(quarters, dimes,nickels,pennies):

    return to_string_from_tuple((quarters,dimes,nickels,pennies))


if __name__ == "__main__":
    print("this program is meant to be run from another script")