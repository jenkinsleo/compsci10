valid_response_count = 0
while True:
    response = input("")
    try:
        value = float(response)
        valid_response = True
        valid_response_count += 1
    except:
        value = 0
        valid_response = False
        valid_response_count += 0
    if response.upper() == 'Q':
        break 

print("valid numbers: " + str(valid_response_count))