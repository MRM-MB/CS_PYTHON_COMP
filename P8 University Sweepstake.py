# Checker for the right input
while True:
    user_input = input("Please insert a number(int): ")
    try:
        n = int(user_input)
        if(n > 0):
            break
    except ValueError:
        print("Error: This is not an integer")

def WinnerWinnerChickenDinner(n):
    # List of StudentsParticipants
    StudentsParticipants = list(range(1, n + 1))
    LeftRight = True # Control Direction
    
    while len(StudentsParticipants) > 1:
        if LeftRight:
            # Eliminate from LeftRight
            StudentsParticipants = [StudentsParticipants[i] for i in range(len(StudentsParticipants)) if i % 2 == 1]
        else:
            # Eliminate from RightLeft
            StudentsParticipants = [StudentsParticipants[i] for i in range(len(StudentsParticipants)) if (len(StudentsParticipants) - i - 1) % 2 == 1]
        
        # Switch Direction
        LeftRight = not LeftRight
    
    # Left over student -> Winner
    return StudentsParticipants[0]

winner = WinnerWinnerChickenDinner(n)
print(winner)