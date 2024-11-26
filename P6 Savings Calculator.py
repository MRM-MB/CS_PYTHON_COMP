# Checker for the right input
while True:
    user_input = input("Please insert the Laptop price (DKK): ")
    try:
        x = int(user_input)
        if(x > 0):
            break
    except ValueError:
        print("Error: This is not an integer")

# Checker for the right input
while True:
    user_input = input("Please insert the amount of money you saved (DKK): ")
    try:
        y = int(user_input)
        if(y > 0):
            break
    except ValueError:
        print("Error: This is not an integer")
    
week_count = 0      # Week count set to zero

while(y < x):
    if(week_count == 0):           # week 0 he's making money (condition need because 0%4 == 0 as well)
        y += (5/100)*y
        week_count += 1            # increase week count by 1
    elif(week_count % 4 == 0):     # weeks that are multiple of 4: he's losing money
        y -= (3/100)*y
        week_count += 1            # increase week count by 1
    else:                          # any other weeks: he's earning money
        y += (5/100)*y
        week_count += 1            # increase week count by 1

print(week_count)
