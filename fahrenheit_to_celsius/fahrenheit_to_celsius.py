#super simple program to convert fahrenheit to celsius

#gets temp in fahrenheit
temperature_fahrenheit = float("".join(input("What is the temperature in Fahrenheit?:").replace('"', '')))

#converts to celsius
celsius_temperature = (temperature_fahrenheit - 32) * (5/9)

#outputs
#print(f"The temperature in Celsius is {round(celsius_temperature, 1)}")

#unit test asks for just the rounded float as output
print(round(celsius_temperature, 1))