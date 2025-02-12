# Input reading
n, h = map(int, input().split())  # Read the number of friends and fence height
heights = list(map(int, input().split()))  # Read the heights of friends

# Initialize the width of the road
total_width = 0

# Calculate the total width based on each friend's height
for height in heights:
    if height > h:
        total_width += 2  # The person bends down and takes width 2
    else:
        total_width += 1  # The person stands up and takes width 1

# Output the minimum valid width of the road
print(total_width)
