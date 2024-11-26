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


"""
# Number of courses and rules
def read_input():
    while True:
        try:
            num_courses = int(input("Please insert the total number of courses: "))
            if num_courses > 0:
                break
        except ValueError:
            print("Error: Please enter a valid positive integer.")
    
    while True:
        try:
            num_rules = int(input("Please insert the number of rules: "))
            if num_rules >= 0:
                break
        except ValueError:
            print("Error: Please enter a valid non-negative integer.")

    rules = []
    print(f"Please input {num_rules} pairs of prerequisites:")
    for _ in range(num_rules):
        try:
            a, b = map(int, input().split())
            if 0 <= a < num_courses and 0 <= b < num_courses:
                rules.append((a, b))
            else:
                print(f"Error: Both values must be between 0 and {num_courses - 1}.")
        except ValueError:
            print("Error: Invalid input format. Please enter two integers separated by a space.")
    return num_courses, rules


# Topological sort using Depth-First Search (DFS)
def find_course_order(num_courses, prerequisites):
    # adjacency list
    adj_list = [[] for _ in range(num_courses)]
    for a, b in prerequisites:
        adj_list[b].append(a)

    # -> Use an array to detect cycles (0 for unvisited, 1 for visiting, 2 for visited)
    def dfs(course, visited, result):
        if visited[course] == 1:  # Cycle detected
            return False
        if visited[course] == 2:  # Already processed
            return True

        visited[course] = 1  # Mark as visiting
        for neighbor in adj_list[course]:
            if not dfs(neighbor, visited, result):
                return False
        visited[course] = 2  # Mark as visited
        result.append(course)  # Add course to result
        return True

    # Main function logic
    visited = [0] * num_courses
    result = []

    for course in range(num_courses):
        if visited[course] == 0:
            if not dfs(course, visited, result):
                return []  # empty list
    return result

num_courses, rules = read_input()
solution = find_course_order(num_courses, rules)
print(solution)
"""
