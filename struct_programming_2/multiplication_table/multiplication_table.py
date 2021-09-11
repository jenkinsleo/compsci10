#simple program to make a multiplication table 

#gets parameters from user then converts into list
def get_params():
    start_number = int(input("Starting number: "))
    end_number = int(input("Ending number: "))

    start_factor = int(input("Starting factor: "))
    end_factor = int(input("Ending factor: "))

    #returns 2 lists (number, factor) of ranges based on the inputs
    return list(range(start_number, end_number + 1)), list(range(start_factor, end_factor + 1))

def create_data(numbers, factors):
    multiple_dict = {'numbers': numbers, 'factors':factors}

    for x in factors:
        factor_list = []
        for y in numbers:
            factor_list.append(x*y)

        multiple_dict[x] = factor_list

    return multiple_dict

def format_data():
    pass


numbers, factors = get_params()
print(create_data(numbers, factors))