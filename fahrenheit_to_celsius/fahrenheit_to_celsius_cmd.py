#simple way to run fahrenheit_to_celsius.py from the command line

#args: fahrenheit

#example command: python fahrenheit_to_celsius_cmd.py 100
#example return: 37.78



#imports neccessary
import fahrenheit_to_celsius
import sys

#creates a new triangle instance
conversion = fahrenheit_to_celsius.Convert()

#sets the base and height from arguments
conversion.f = float(sys.argv[1])

response = conversion.calculate_conversion()

print(response)