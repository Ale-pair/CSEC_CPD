def count_problems_to_solve(n, problems):
    solved_count = 0
    for problem in problems:
        # Sum the values of Petya's, Vasya's, and Tonya's confidence
        if sum(problem) >= 2:
            solved_count += 1
    return solved_count

# Reading input
n = int(input())  # number of problems
problems = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
print(count_problems_to_solve(n, problems))
