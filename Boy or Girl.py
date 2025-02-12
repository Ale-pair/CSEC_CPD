def determine_gender(username):
    # Step 1: Create a set from the username to find distinct characters
    distinct_characters = set(username)
    
    # Step 2: Count the number of distinct characters
    distinct_count = len(distinct_characters)
    
    # Step 3: Determine gender based on whether the count is odd or even
    if distinct_count % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

# Read the username from input
username = input().strip()

# Call the function with the username
determine_gender(username)
