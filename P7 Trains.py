"""
* We can use any wagon length any number of times
* The station length must be matched exactly and it equals the Train Length


"Representation"
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
f(x) -> Number of ways to assemble the train of length x
f(Train Length) = Sum [ f(Train Length - Wagon Legth) ]; (Train Length >= Wagon Length)
                    |
                    ----> For each Wagon Length

"Important"
‾‾‾‾‾‾‾‾‾‾‾
f(0) = 1; There is only one way to assemble it, with no wagons

"Example" -> Train Length (5), Two Wagons of Length [3, 2]
‾‾‾‾‾‾‾‾‾
f(1) = 0; (3 and 2) > 1 -> Not possible to form a (Train of Length == 1) in this case

*f(5) = f(3) + f(2);

|f(3) = f(3-2) = f(1) = 0
|f(3) = f(3-3) = f(0) = 1
- Total Sum - f(3) = 1

|f(2) = f(2-3) = f(-1) = 0 -> Not possible
|f(2) = f(2-2) = f(0) = 1
- Total Sum - f(2) = 1

*f(5) = 1 + 1 = 2
"""

""" -> RECURSIVE APPROACH (5.041819334030151 seconds)
       ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
def LetsMakeATrain(TrainLength, Wagons):
    # Length == 0 (No wagons) -> Only One Way
    if TrainLength == 0:
        return 1
    if TrainLength < 0: # Negative case -> No Way
        return 0
    
    # Wagons Sum
    NumberOfWays = 0
    for WagonLength in Wagons:
        NumberOfWays += LetsMakeATrain(TrainLength - WagonLength, Wagons)
    return NumberOfWays
"""

# -> BOTTOM-UP "DYNAMIC PROGRAMMING" (0.0 seconds)
def LetsMakeATrain(TrainLength, Wagons):
    # Table for storing the number of ways to form each Train Length
    ways = [0] * (TrainLength + 1)
    ways[0] = 1  # -> Only One Way for Length == 0 (no wagons)

    for length in range(1, TrainLength + 1):
        for WagonLength in Wagons:
            if length - WagonLength >= 0:
                ways[length] += ways[length - WagonLength]
    return ways[TrainLength]

# Input
Wagons = [2, 5, 10, 50, 100]
TrainLength = 6800
print("\nThe train 🚂  must be", LetsMakeATrain(TrainLength, Wagons), "u long.")