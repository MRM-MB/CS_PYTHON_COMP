while True:
    user_input = input("Please insert the number of computers: ")
    try:
        n = int(user_input)
        break
    except ValueError:
        print("Error: This is not an integer")

while True:
    user_input = input("Please insert the number of cables: ")
    try:
        k = int(user_input)
        break
    except ValueError:
        print("Error: This is not an integer")
    
num_of_hours = 0
num_of_Linux_computers = 1
n -= 1

while(n > 0):
    if(num_of_Linux_computers <= k):
        n -= num_of_Linux_computers
        num_of_Linux_computers += num_of_Linux_computers
        num_of_hours += 1
    else:
        n -= k
        num_of_Linux_computers += k
        num_of_hours += 1

print(num_of_hours)