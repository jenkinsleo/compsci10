#simple way to run area_of_a_triangle.py from the command line

#args: base, height

#example command: python area_of_a_triangle.py 10 20
#example return: 100.0



#imports neccessary
import area_of_a_triangle
import sys

#creates a new triangle instance
triangle = area_of_a_triangle.Triangle()

#sets the base and height from arguments
triangle.base = float(sys.argv[1])
triangle.height = float(sys.argv[2])

area = triangle.calculate_area()

print(area)