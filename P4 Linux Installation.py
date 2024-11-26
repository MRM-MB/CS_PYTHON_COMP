# Checker for the right input
while True:
    user_input = input("Please insert the number of computers: ")
    try:
        n = int(user_input)
        break
    except ValueError:
        print("Error: This is not an integer")

# Checker for the right input
while True:
    user_input = input("Please insert the number of cables: ")
    try:
        k = int(user_input)
        break
    except ValueError:
        print("Error: This is not an integer")
    
num_of_hours = 0                # hours counter
num_of_Linux_computers = 1      # number of computer updated with Linux
n -= 1                          # we assume one of the computer has already the latest Linux version

while(n > 0):
    if(num_of_Linux_computers <= k):                
        n -= num_of_Linux_computers     # number of computers that still need the update
        num_of_Linux_computers += num_of_Linux_computers       # new number of computer with the latest version of Linux
        num_of_hours += 1               # hours counter updated
    else:
        n -= k                          # number of computers that still need the update
        num_of_Linux_computers += k     # new number of computer with the latest version of Linux
        num_of_hours += 1               # hours counter updated

print(num_of_hours)