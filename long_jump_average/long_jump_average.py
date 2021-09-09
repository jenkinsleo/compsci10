#a basic way to average 4 jumps in a long jump competition
#takes 4 floats and calculates based on the farthest 3 jumps
farthest_jumps = 3
amount_jumps = 4

def long_jump_inputs():
    #takes the inputs based off of amount_jumps
    #stores all the jumps
    jumps = []
    #takes the inputs
    for x in range(0, amount_jumps):
        jumps.append(float(input(f"Enter result for long jump ({x + 1}): ")))  #note range starts on 0 so 1 is added for user experience

    return jumps

def long_jump_calculations(jumps):
    #calculates the farthest jumps based on variable farthest_jumps

    #sorts the list from greatest to smallest and takes the top amount based off of farthest_jumps
    jumps.sort(reverse=True)  #reverse changes the direction of the sorting (default is smallest to greatest)

    top_jumps = jumps[:farthest_jumps]

    #averages the top jumps
    overall = 0.00
    for o in top_jumps:
        overall = overall + float(o)
    
    #averages and returns
    averaged = overall / farthest_jumps

    return averaged

if __name__ == "__main__":
    jumps = long_jump_inputs()

    print(long_jump_calculations(jumps))
