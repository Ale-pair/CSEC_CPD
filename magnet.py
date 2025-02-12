def count_groups(n, magnets):
    # Initialize the number of groups with 1, since the first magnet starts the first group.
    groups = 1
    
    # Compare each magnet with the previous one
    for i in range(1, n):
        if magnets[i] != magnets[i-1]:
            groups += 1
    
    return groups

# Input processing
n = int(input())  # Number of magnets
magnets = [input().strip() for _ in range(n)]  # List of magnet configurations

# Output the result
print(count_groups(n, magnets))
