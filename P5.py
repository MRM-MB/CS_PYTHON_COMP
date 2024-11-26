def IsItPolindrome(word):
    def YesPolindrome(inv):
        return inv == inv[::-1] # Resturns inverted word
    
    palindromes = set() # Check for uniqueness
    
    for i in range(len(word)):
        for j in range(i + 2, len(word) + 1):
            miniword = word[i:j] # ----------------------------- WHAT??
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

# Example usage
IsItPolindrome("CommOdore64")