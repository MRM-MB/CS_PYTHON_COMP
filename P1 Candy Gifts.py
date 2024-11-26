while True:
    user_input = input("Please insert the number of packages prepared by Bob: ")
    try:
        number = int(user_input)
        break
    except ValueError:
        print("Error: This is not an integer")

if (number % 2 == 0):
    x = number / 2
    y = (number / 2) + 1
    print(number // 2) # Number of Children
    while(x != 0):
        print(f"2 {int(x)} {int(y)}")
        x -= 1
        y += 1
else: 
    print(f"{number // 2 + 1}") # Number of Children
    print(f"1 {number}")
    num = number - 1
    x = num / 2
    y = (num / 2) + 1
    while(x != 0):
        print(f"2 {int(x)} {int(y)}")
        x -= 1
        y += 1