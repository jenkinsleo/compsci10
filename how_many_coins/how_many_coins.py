#simple program to calculate the change needed

#creates a dictionary of all the supported coins and their corresponding values


#can support loonies and toonies easily as well
supported_coins = {"quarter": 0.25, "dimes": 0.1, "nickel": 0.05, "penny": 0.01}

#gets user input and converts into float
def get_money():
    money = input("Enter the amount?:")

    #unit test on macos adds extra quotes this filters it out
    return float("".join(money.replace('"', '')))
    

def calculate_coins(money):
    #starts with the higher value coins then works down the the lower value by bringing over the remainder

    new_money = money
    final_coins = {}

    for key in supported_coins:
        #gets how many of the selected coins will fit and adds that to the new dict
        final_coins[key], remainder = divmod(new_money, supported_coins[key])

        #for debugging purposes will print step by step checking every coin
        #print(f"Testing if {supported_coins[key]} ({key}) goes into {new_money}, {final_coins[key]}")
        
        #rounds and adds to the variable to be checked again with the next lowest coin interval
        new_money = round(remainder, 2)

    return final_coins

def create_pretty(money_list):
    #this just formats this into a pretty list

    return f'quarters:{int(money_list["quarter"])}; dimes:{int(money_list["dimes"])}; nickels:{int(money_list["nickel"])}; pennies:{int(money_list["penny"])}'


if __name__ == "__main__":
    money = get_money()
    money_list = calculate_coins(money)

    print(create_pretty(money_list))

    #print(money_list)