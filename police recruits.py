def untreated_crimes(n, events):
    available_officers = 0
    untreated_crimes = 0

    for event in events:
        if event == -1:
            if available_officers > 0:
                available_officers -= 1  # One officer handles the crime
            else:
                untreated_crimes += 1  # No officer available, crime goes untreated
        else:
            available_officers += event  # Recruiting new officers

    return untreated_crimes


# Input reading
n = int(input())  # Number of events
events = list(map(int, input().split()))  # List of events

# Output the result
print(untreated_crimes(n, events))
