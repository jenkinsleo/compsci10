#!/usr/bin/env python3

#a basic way to average AMOUNT_JUMPS - 1 in a long jump competition
#smallest input will be ignored
AMOUNT_JUMPS = 4

def long_jump_inputs():
    #takes the inputs based off of AMOUNT_JUMPS
    #stores all the jumps
    jumps = []
    #takes the inputs
    for x in range(0, AMOUNT_JUMPS):
        input_data = input(f"Enter result for long jump ({x + 1})?: ") #note range starts on 0 so 1 is added for user experience
        jumps.append(float("".join(input_data.replace('"', ''))))  #the unit tests adds some weird quotes might be a mac thing but this fixes it

        #jumps.append(input_data)

    return jumps

def long_jump_calculations(jumps):

    top_jumps = jumps

    #gets the total sum and ignores the smallest input
    overall = sum(top_jumps)
    overall = overall - min(jumps)
    
    #averages and returns
    averaged = overall / (AMOUNT_JUMPS - 1)

    return averaged

if __name__ == "__main__":
    jumps = long_jump_inputs()

    print("Average = " + str(long_jump_calculations(jumps)))
