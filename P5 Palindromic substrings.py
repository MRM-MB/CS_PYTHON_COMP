# Checker for the right input
while True:
    user_input = input("Please insert a word: ").strip()  # Remove leading and trailing whitespace
    if isinstance(user_input, str) and len(user_input) > 0:  # Check that it is a string and that it is not empty
        break
    else:
        print("Error: This is not a valid word. Please try again.")

def IsItPolindrome(word):
    def YesPolindrome(inv):
        return inv == inv[::-1] # Resturns inverted word
    
    palindromes = set() # Check for uniqueness
    
    for i in range(len(word)):
        for j in range(i + 2, len(word) + 1):
            miniword = word[i:j]                # string slicing (it tries every single word)
            if YesPolindrome(miniword):
                palindromes.add(miniword)
    
    # Sort by Alphabet order
    AlphabeticallySorted = sorted(palindromes)
    
    # Print results
    if AlphabeticallySorted:
        for palindrome in AlphabeticallySorted:
            print(palindrome)
    else:
        print("No Palindromes")

IsItPolindrome(user_input)