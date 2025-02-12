def update_birds(n, a, m, shots):
    for x, y in shots:
        x -= 1  # Convert to 0-based index
        y -= 1  # Convert to 0-based index
        # Birds to the left of the shot bird jump up
        if x > 0:
            a[x-1] += y
        # Birds to the right of the shot bird jump down
        if x < n-1:
            a[x+1] += a[x] - y - 1
        # The shot bird dies
        a[x] = 0
    return a

# Read input
n = int(input())
a = list(map(int, input().split()))
m = int(input())
shots = [tuple(map(int, input().split())) for _ in range(m)]

# Update the number of birds after each shot
result = update_birds(n, a, m, shots)

# Print the result
for res in result:
    print(res)
