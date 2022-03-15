TAX = 0.82
WORK_WEEK = 40
OVERTIME_PAY_RATE = 1.5

#I
hours_worked = float(input("hours worked?:"))
wage = float(input("hourly wage?:"))
exempt_taxes = str(input("exempt taxes?:"))

overtime_pay = wage * OVERTIME_PAY_RATE
#P
if hours_worked - WORK_WEEK > 0:
   overtime_hours = hours_worked - WORK_WEEK
   hours = hours_worked - overtime_hours
   gross_earnings = hours * wage + overtime_hours * overtime_pay
else:
   gross_earnings = hours_worked * wage

if exempt_taxes.upper() == 'Y':
   net_earnings = gross_earnings
else:
   net_earnings = gross_earnings * TAX

#O
format_earnings = '$' + '{:.2f}'.format(net_earnings)
print("Net wage is " + format_earnings)

