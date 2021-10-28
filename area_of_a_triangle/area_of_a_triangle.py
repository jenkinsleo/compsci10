#super simple program to take 2 input and calculate the area of a triangle
#takes 2 inputs
base_input = float("".join(input("What is the base?:").replace('"', '')))
height_input = float("".join(input("What is the height?:").replace('"', '')))

#calculates
area = base_input * height_input / 2

#prints output rounded
print(f"The area is {round(area, 2)}")