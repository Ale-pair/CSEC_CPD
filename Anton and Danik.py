def determine_winner(n, s):
    # Count how many times 'A' (Anton) and 'D' (Danik) appear in the string
    anton_wins = s.count('A')
    danik_wins = s.count('D')
    
    # Determine the result based on the counts
    if anton_wins > danik_wins:
        print("Anton")
    elif danik_wins > anton_wins:
        print("Danik")
    else:
        print("Friendship")

# Reading input
n = int(input())  # number of games
s = input()       # string representing the results of games

determine_winner(n, s)
