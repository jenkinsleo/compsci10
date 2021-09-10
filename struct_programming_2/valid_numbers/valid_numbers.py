#simple program to count the number of valid numbers

count = 0
while True:
    num = input("Enter a number (Q to quit): ")

    try:
        num = float(num)
        count = count + 1
    except:
        if num.upper() == "Q":
            print(f"Valid Numbers: {count}")
            break
        else:
            print("Not a valid number")

            