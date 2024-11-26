list_of_rules = []
solution_list = []
x = 0               # number of courses (default 0)
r = 0               # number of rules (default 0)

# Checker for the course's number
while True:
    user_input = input("Please insert the total number of courses: ")
    try:
        x = int(user_input)
        if(x > 0):
            break
    except ValueError:
        print("Error: This is not an integer")

# Checker for the rule's number
while True:
    user_input = input("Please insert the number of rules: ")
    try:
        r = int(user_input)
        if(x >= 0):
            break
    except ValueError:
        print("Error: This is not an integer")

# Checker for the rules
for rule in range(r):
    user_input = input("Please enter a tuple of two numbers separated by a space: ")
    # Try to split the input into two parts
    a, b = user_input.split()
    
    # Convert both parts to numbers (int)
    a = int(a)
    b = int(b)
    
    # If the process is successful, create the tuple and exit the loop
    result = (a, b)
    list_of_rules.append(result)

for i in range(x):
    solution_list.append(i)

for index, tup in enumerate(list_of_rules):
    index1 = solution_list.index(tup[0])    # 0
    index2 = solution_list.index(tup[1])    # 2
    if index2 > index1:
        solution_list[index1], solution_list[index2] = solution_list[index2], solution_list[index1]     # Swap the two number


print(solution_list)