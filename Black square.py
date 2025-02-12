def calculate_calories(a1, a2, a3, a4, s):
    total_calories = 0
    for char in s:
        if char == '1':
            total_calories += a1
        elif char == '2':
            total_calories += a2
        elif char == '3':
            total_calories += a3
        elif char == '4':
            total_calories += a4
    return total_calories

# Input reading
a1, a2, a3, a4 = map(int, input().split())  # The calories for strips 1, 2, 3, and 4
s = input()  # The string representing the game events

# Output the result
print(calculate_calories(a1, a2, a3, a4, s))
