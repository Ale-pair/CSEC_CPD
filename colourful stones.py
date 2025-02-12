def final_position(s, t):
    # Start at the first stone (0-based index)
    current_position = 0
    
    # Process each instruction
    for instruction in t:
        # If the current stone matches the instruction, move to the next stone
        if s[current_position] == instruction:
            current_position += 1
    
    # Since the position is 1-based, return current_position + 1
    return current_position + 1

# Input reading
s = input().strip()
t = input().strip()

# Output the final position
print(final_position(s, t))
