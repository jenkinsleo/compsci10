#a simple program to calculate an employees earnings

#overtime is payed after the work week is passed
work_week = 40
overtime_percent = 1.5
#employee is automatically taxed unless specified otherwise
tax_percent = 18

#gets input from user
def get_params():
    hours = float(input("How many hours worked?:"))
    wage = float(input("What is the pay per hour?:"))
    tax_exempt = str(input("Are taxes exempt (Y / N)?:")).upper()

    #returns true / false based on response
    if tax_exempt == "Y":
        tax_exempt = True

    else:
        tax_exempt = False

    return hours, wage, tax_exempt

#calculates the pay and returns a float value of either net or gross earnings
def calculate_pay(hours,wage,tax_exempt):
    #first checks how much should be payed as overtime
    if hours > 40:
        overtime_hours = hours - 40
        base_pay = (overtime_hours * wage) * overtime_percent

        hours = hours - overtime_hours

    else:
        base_pay = 0

    #calculates the normal work week pay
    base_pay = base_pay + hours * wage

    #checks if tax exempt and if not subtracts the taxes and finally returns
    if tax_exempt:
        return round(base_pay, 2)

    else:
        taxed_pay_percent = 1 - (tax_percent / 100)
        base_pay = base_pay * taxed_pay_percent

        return round(base_pay, 2)


if __name__ == "__main__":
    hours, wage, tax_exempt = get_params()
    net_earnings = calculate_pay(hours, wage, tax_exempt)

    print(net_earnings)

