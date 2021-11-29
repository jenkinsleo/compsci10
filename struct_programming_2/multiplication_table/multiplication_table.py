#simple program to make a multiplication table


#gets inputs
start_factor = int(input("Starting number ?: "))
end_factor = int(input("Ending number ?: "))
start_number = int(input("Starting Factor ?: "))
end_number = int(input("Ending Factor ?: "))

output = '   '

if start_number <= end_number:
    for num in range(start_number, end_number + 1):
        output += '{:>5}'.format(str(num))
    print('{:8}'.format(output))
    print("---" + "-" * 5 * (end_number - start_number + 1))

for row in range(start_factor, end_factor + 1):
    output = ""
    output += '{0:>3}'.format(str(row) + ":")
    for col in range(start_number, end_number + 1):
        output += '{0:>5}'.format(str(col*row))
    print(output)