start_n = int(input('Start :'))
end_n = int(input('End :'))
final_number = 0
output = ""

if start_n <= end_n:
    for number in range(start_n, end_n + 1):
        final_number += number
        
        if number == start_n:
            output == f"{number}"
        else:
            output += f" + {number}"
    output += f" = {str(final_number)}"
    output = (str(start_n) + output)
else:
    output = ('INVALID')

print(output)

