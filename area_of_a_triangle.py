#simple program to calculate the area of a triangle based off the base and height
#uses the formula h*b/2

class Triangle():
    
    height = 0
    base = 0

    #perfoms the calculation and returns answer
    def calculate_area(self):
        area = self.height * self.base / 2

        return float(area)

    #gets the parameters needed for height and base and calculates then returns

    def get_params(self):
        #gets height from user
        self.height = int(input("Height of triangle: "))

        #gets base of triangle
        self.base = int(input("Base of triangle: "))

    


    #basic init doesnt do much
    def __init__(self):
        #print("New triangle has been created!")

        pass

        


if __name__ == "__main__":
    #on run of the script asks the user for height and base, perfoms calculation of area then prints response
    new_triangle = Triangle()
    new_triangle.get_params()
    
    #perfoms calculation
    area = new_triangle.calculate_area()
    print(area)


