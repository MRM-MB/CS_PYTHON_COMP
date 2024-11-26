"""

# STEP 1: [1, 2, 3, 4, 5, 6, 7, 8] -> Left To Right and take out odd postion (since we start from the first number on the left)

# STEP 2: [2, 4, 6, 8] -> Right To Left (Transverse) and take out again odd position (starting from the first postion on the right)

[2, 6] -> Repeat STEPS 1 and 2 as necessary to get the winner

[6] -> WINNER

"""

def WinnerWinnerChickenDinner(winner):
    # Left to Right movement for the list of numbers
    LeftToRight = True
    start = 1
    move = 1
    StudentsNumbers = winner # All the students receive a number assigned to them which is stored in an ordered array
    
    while StudentsNumbers > 1:
        if LeftToRight or StudentsNumbers % 2 == 1: # Check for the direction and odd number for the remaining students
            # Update start when from Left to Right
            start += move
        # Double the move and halve the StudentsNumbers
        move *= 2
        StudentsNumbers //= 2
        # Switch direction
        LeftToRight = not LeftToRight
    return start

# Take an input
while True:
    try:
        winner = int(input("\nEnter number of students (int): "))
        if winner > 0:
            break
        print("\nThe number must be greater than 0")
    except ValueError:
        print("\nThe number must be an integer 🤔")
print("\n🎉 🥳 Congratulations, you won student number:", WinnerWinnerChickenDinner(winner))
