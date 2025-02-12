import math

def probability_of_dot_winning(Y, W):
    # Find the maximum value of Y and W
    max_value = max(Y, W)
    
    # Number of successful outcomes for Dot
    successful_outcomes = 6 - max_value + 1
    
    # The total possible outcomes is always 6 (since the die has 6 faces)
    total_outcomes = 6
    
    # Simplify the fraction using GCD
    gcd = math.gcd(successful_outcomes, total_outcomes)
    numerator = successful_outcomes // gcd
    denominator = total_outcomes // gcd
    
    # Return the result in the form of "A/B"
    return f"{numerator}/{denominator}"

# Input reading
Y, W = map(int, input().split())

# Output the result
print(probability_of_dot_winning(Y, W))
