#simple program to get movie preferences and format nicely a movie ticket
LINE_SPLIT = "\n"

ADULT_PRICE = 12.50
CHILD_PRICE = 8.25
SENIOR_DISCOUNT_DECIMAL = 0.75

#gets the movie preferences (movie name, number of adults, number of children, number of seniors) then calculates total and returns all

def movie_preferences():
    movie_name = str(input("Movie name?:"))
    num_adults = int(input("Number of adults?:"))
    num_children = int(input("Number of children?:"))
    num_seniors = int(input("Number of seniors?:"))

    #the prices per tickets
    adult_ticket = ADULT_PRICE
    child_ticket = CHILD_PRICE
    #percentage that the seniors get off (i could have put just the cost but that seemed too boring)
    senior_percentage = SENIOR_DISCOUNT_DECIMAL

    #adult total cost
    adult_cost = adult_ticket * num_adults

    #child total cost
    child_cost = child_ticket * num_children

    #senior cost is seniors x adult price x discount
    senior_cost = float(num_seniors * adult_ticket * senior_percentage)

    #total cost
    total_cost = adult_cost + child_cost + senior_cost

    #values will be returned movie_name, num_adults, num_children, num_seniors, total_cost
    return movie_name, num_adults, num_children, num_seniors, total_cost

def format_ticket(name, adults, child, senior, cost):
    #creates a list for each individual line then at the end joins together with line split
    ticket = []

    #first line starts with 30 dashes
    first_line = "-" * 30
    ticket.append(first_line)
    
    #second line is the movie name centered 
    second_line = "|" + '{:^28}'.format("*** " + name + " ***") + "|"
    ticket.append(second_line)

    #third, fourth, fifth line is number of adults, children, seniors
    third_line = "| " + '{:13}'.format("Adults:") + '{:>13}'.format(adults) + " |"
    fourth_line = "| " + '{:13}'.format("Children:") + '{:>13}'.format(child) + " |"
    fifth_line = "| " + '{:13}'.format("Seniors:") + '{:>13}'.format(senior) + " |"

    ticket.append(third_line)
    ticket.append(fourth_line)
    ticket.append(fifth_line)

    #last line is the cost centered to the right as well 
    total_price = round(cost, 2)
    format_total_price = "{:.2f}".format(total_price)
    sixth_line = "| " + '{:16}'.format("Total:") + "{:>4}".format(str("$ ")) + "{:>6}".format(format_total_price) + " |"
    ticket.append(sixth_line)

    #finish off with the closing dashes
    seventh_line = "-" * 30
    ticket.append(seventh_line)

    #combines the ticket into one large string with \n

    return LINE_SPLIT.join(ticket)



if __name__ == "__main__":
    movie_name, num_adults, num_children, num_seniors, total_cost = movie_preferences()
    print(format_ticket(movie_name, num_adults, num_children, num_seniors, total_cost))