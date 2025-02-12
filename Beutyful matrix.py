def minimum_moves_to_center(matrix):
    # Loop through the matrix to find the position of '1'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                # Calculate the Manhattan distance to the center (3,3)
                return abs(i - 2) + abs(j - 2)

# Reading the input
matrix = [list(map(int, input().split())) for _ in range(5)]

# Calculate and print the result
print(minimum_moves_to_center(matrix))
