#simple program to convert from fahrenheit to celsius

class Convert():
    #f for fahrneheit
    
    f = 0

    def calculate_conversion(self):

        #c for celsius

        c = (self.f - 32) * (5 / 9)

        #rounds to one decimal place
        c_round = round(c, 2)

        #c_round = float("{:.2f}".format(c))

        return c_round

    def format(self, conversion):
        #note f strings dont work in python 2
        #return "The temperature in Celsius is " + conversion
        return f"The temperature in Celsius is {conversion}"



    def get_params(self):

        #gets fahrenheit from user
        temp_degree = float(input("Temperature in Fahrenheit: "))

        #makes sure temp is above or equal to 0
        if temp_degree >= 0:
            self.f = temp_degree
        else:
            print("The temperature must be 0 degrees or greater")
            quit()

    def __init__(self):
        #print("testing")
        pass

if __name__ == "__main__":
    new_conversion = Convert()

    new_conversion.get_params()

    #calculates based off of params then formats the calculated respone to look more pretty
    print(new_conversion.format(new_conversion.calculate_conversion()))

