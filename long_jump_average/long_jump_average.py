#!/usr/bin/env python3

#a basic way to average 4 jumps in a long jump competition
#takes 4 floats and calculates based on the farthest 3 jumps
FARTHEST_JUMPS = 3
AMOUNT_JUMPS = 4

def long_jump_inputs():
    #takes the inputs based off of AMOUNT_JUMPS
    #stores all the jumps
    jumps = []
    #takes the inputs
    for x in range(0, AMOUNT_JUMPS):
        input_data = input(f"Enter result for long jump ({x + 1})?: ") #note range starts on 0 so 1 is added for user experience
        jumps.append(float("".join(input_data.replace('"', ''))))  #the unit tests adds some weird quotes might be a mac thing but this fixes it

    return jumps

def long_jump_calculations(jumps):
    #calculates the farthest jumps based on variable FARTHEST_JUMPS

    #sorts the list from greatest to smallest and takes the top amount based off of FARTHEST_JUMPS
    jumps.sort(reverse=True)  #reverse changes the direction of the sorting (default is smallest to greatest)

    top_jumps = jumps[:FARTHEST_JUMPS]

    #averages the top jumps
    overall = 0.00
    for o in top_jumps:
        overall = overall + float(o)
    
    #averages and returns
    averaged = overall / FARTHEST_JUMPS

    return averaged

if __name__ == "__main__":
    jumps = long_jump_inputs()

    print("Average = " + str(long_jump_calculations(jumps)))
