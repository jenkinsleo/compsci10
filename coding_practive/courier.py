def calculate_cost(weight, priority, destination):

    cost = calculate_weight(weight)

    cost = calculate_priority(cost, priority)

    cost = calculate_destination(cost,destination)


    return cost

def calculate_weight(weight):

    if weight <= 100:
        cost = 0.50
    elif weight > 100 and weight <=200:
        cost = 0.75
    else:
        cost = 1.00

    return cost


def calculate_priority(cost, type):
    
    if type == 'Priority' or type.upper() == 'P':
        new_cost = (cost * 1.5)

    elif type == 'express' or type.upper() == 'E':
        new_cost = (cost * 2.5)

    else:
        new_cost = cost

    return new_cost

def calculate_destination(cost,type):
    if type == 'international' or type.upper() == "I":
        new_cost = cost + 2.00
    else :
        new_cost = cost

    return new_cost


if __name__ == "__main__":
    #inputs
    weight = int(input("Weight?:"))
    priority = str(input("Priority?:"))
    destination = str(input("Destination?:"))

    
    #processing
    cost = calculate_cost(weight,priority,destination)
    #output
    print('${:.2f}'.format(cost))