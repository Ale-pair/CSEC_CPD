def minimum_shovels(k, r):
    # We iterate over the number of shovels
    for n in range(1, 11):  # We only need to check for n from 1 to 10
        total_cost = n * k
        # Check if the total cost is divisible by 10 or ends with r
        if total_cost % 10 == 0 or total_cost % 10 == r:
            return n  # Return the number of shovels
    
    # If not found within the first 10, we know we can always pay with 10 shovels
    return 10

# Input
k, r = map(int, input().split())

# Output the result
print(minimum_shovels(k, r))
