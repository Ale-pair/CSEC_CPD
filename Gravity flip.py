n = int(input())  # Read the number of columns
a = list(map(int, input().split()))  # Read the number of cubes in each column

a.sort()  # Sort the list to simulate the gravity shift

print(*a)  # Print the sorted list
