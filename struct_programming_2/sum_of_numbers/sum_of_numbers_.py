start_variable, end_variable = int(input("Start number: ")), int(input("End number: ")) + 1;before_equal_sign = " + ".join(list(map(str, list(range(start_variable, end_variable)))));total = before_equal_sign + " = " + str(sum(range(start_variable,end_variable))) if start_variable < end_variable else "INVALID";print(total) #assigns variables to be used for the ranges, end number is +1 because range doesnt include it nomrally, creates a new string before_equal_sign that is joining a list of string of a range (split by +), creates a final string that includes the before_equal_sign plus the final calculation split by =, tests if params are invalid, finally prints