#simple program to count the number of valid numbers

count = 0
sum = 0
min = float
max = 0
while True:
    num = input("Enter a number (Q to quit): ")

    try:
        num = float(num)
        count = count + 1
        sum = sum + num

        if num > max:
            max = num
        else num < min:
            min = num
    except:
        if num.upper() == "Q":
            print(f"Min: {min} Max: {max} Mean: {sum / count}")
            break
        else:
            print("Not a valid number")

            