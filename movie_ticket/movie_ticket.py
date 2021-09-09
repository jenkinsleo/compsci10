#simple program to get movie preferences and format nicely a movie ticket as well as save to a pdf for easy printing


#gets the movie preferences (movie name, number of adults, number of children, number of seniors) then calculates total and returns all

def movie_preferences():
    movie_name = str(input("Movie name: "))
    num_adults = int(input("Number of adults: "))
    num_children = int(input("Number of children: "))
    num_seniors = int(input("Number of seniors: "))

    #the prices per tickets
    adult_ticket = 12.50
    child_ticket = 8.25
    #percentage that the seniors get off (i could have put just the cost but that seemed too boring)
    senior_percentage = 25

    adult_cost = adult_ticket * num_adults
    child_cost = child_ticket * num_children
    senior_cost = num_seniors * adult_ticket * (1.00 - senior_percentage / 100)
    total_cost = adult_cost + child_cost + senior_cost

    #values will be returned movie_name, num_adults, num_children, num_seniors, total_cost
    return movie_name, num_adults, num_children, num_seniors, total_cost

def format_ticket(name, adults, child, senior, cost):
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
    sixth_line = "| " + '{:13}'.format("Total:") + '{:>13}'.format(round(cost, 2)) + " |"
    ticket.append(sixth_line)

    #finish off with the closing dashes
    seventh_line = "-" * 30
    ticket.append(seventh_line)

    #combines the ticket into one large string with \n
    split = "\n"

    return split.join(ticket)



if __name__ == "__main__":
    movie_name, num_adults, num_children, num_seniors, total_cost = movie_preferences()
    print(format_ticket(movie_name, num_adults, num_children, num_seniors, total_cost))