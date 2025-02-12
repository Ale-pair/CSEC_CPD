def min_rotations_to_print_name(name):
    total_rotations = 0
    current_pos = 'a'  # Start at 'a'
    
    for char in name:
        # Calculate positions of current and target characters
        current_index = ord(current_pos) - ord('a')
        target_index = ord(char) - ord('a')
        
        # Calculate clockwise and counterclockwise distances
        clockwise_distance = (target_index - current_index) % 26
        counterclockwise_distance = (26 - clockwise_distance) % 26
        
        # Take the minimum of both distances
        total_rotations += min(clockwise_distance, counterclockwise_distance)
        
        # Update current position to the current character
        current_pos = char
    
    return total_rotations

# Input reading
name = input().strip()

# Output the result
print(min_rotations_to_print_name(name))
