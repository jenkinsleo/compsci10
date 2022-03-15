dollar_amount = (float(input("")))

coin_dict = {"quarters" : 0.25, "dimes" : 0.10, "nickels" : 0.05, "pennies" : 0.01}

#PROCESSING
final_dict = {}
for coin in coin_dict:
    return_coin, dollar_amount = divmod(dollar_amount, coin_dict[coin])
    return_coin = round(return_coin, 2) 
    dollar_amount = round(dollar_amount, 2)
    final_dict[coin] = str(int(return_coin))

#OUTPUT
print("quarters:" + final_dict["quarters"] +"; dimes:" + final_dict["dimes"] +"; nickels:" + final_dict["nickels"] + "; pennies:" + final_dict["pennies"])
