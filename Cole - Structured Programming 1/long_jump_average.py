jumps = []

for x in range(0,4):
    jumps.append(float(input("Jump: ")))

jumps.remove(min(jumps))

average_distance_of_jumps = sum(jumps)/3
print("Average =", round(average_distance_of_jumps, 1))
