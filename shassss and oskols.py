def simulate_shots(n, birds, m, shots):
    for shot in shots:
        xi, yi = shot
        xi -= 1  # Convert to 0-based index
        yi -= 1  # Convert to 0-based index
        
        # Number of birds to move
        birds_to_move_left = yi
        birds_to_move_right = birds[xi] - yi - 1
        
        # Update the number of birds on the current wire
        birds[xi] -= 1
        
        # Move birds to the upper wire if possible
        if xi > 0:
            birds[xi - 1] += birds_to_move_left
        
        # Move birds to the lower wire if possible
        if xi < n - 1:
            birds[xi + 1] += birds_to_move_right

    return birds

# Input
n = int(input())  # number of wires
birds = list(map(int, input().split()))  # initial bird counts on each wire
m = int(input())  # number of shots
shots = [tuple(map(int, input().split())) for _ in range(m)]

# Process the shots
result = simulate_shots(n, birds, m, shots)

# Output the final result
for count in result:
    print(count)
