while True:
    user_input = input("Please insert the Laptop price (DKK): ")
    try:
        x = int(user_input)
        if(x > 0):
            break
    except ValueError:
        print("Error: This is not an integer")

while True:
    user_input = input("Please insert the amount of money you saved (DKK): ")
    try:
        y = int(user_input)
        if(y > 0):
            break
    except ValueError:
        print("Error: This is not an integer")
    
week_count = 0

while(y < x):
    if(week_count == 0):
        y += (5/100)*y
        week_count += 1
    elif(week_count % 4 == 0):
        y -= (3/100)*y
        week_count += 1
    else:
        y += (5/100)*y
        week_count += 1

print(week_count)
