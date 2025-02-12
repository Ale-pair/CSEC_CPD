def min_removals(n, s):
    removals = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            removals += 1
    return removals

# Input reading
n = int(input())  # Number of stones
s = input().strip()  # The string of stones

# Output the result
print(min_removals(n, s))
