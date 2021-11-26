#currency object file
#import this from another script
#made by yours truly
COIN_VALUE = {'quarters':25, 'dimes': 10, 'nickels':5, 'pennies': 1}



def add_coins(quarters, dimes,nickels,pennies=0):
    final_value_in_cents = 0

    final_value_in_cents += quarters * COIN_VALUE['quarters']
    final_value_in_cents += dimes * COIN_VALUE['dimes']
    final_value_in_cents += nickels * COIN_VALUE['nickels']
    final_value_in_cents += pennies * COIN_VALUE['pennies']
    
    final_value_in_dollars = final_value_in_cents / 100
    return final_value_in_dollars


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

    return (final_coins["quarters"], final_coins["dimes"], final_coins["nickels"], final_coins["pennies"])


def to_string_from_tuple(money_list):
    return f'quarters:{int(money_list[0])}; dimes:{int(money_list[11])}; nickels:{int(money_list[2])}; pennies:{int(money_list[3])}'


def to_string(quarters, dimes,nickels,pennies):

    return to_string_from_tuple((quarters,dimes,nickels,pennies))


if __name__ == "__main__":
    print("this program is meant to be run from another script")