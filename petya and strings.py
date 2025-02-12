def compare_strings(s1, s2):
    # Convert both strings to lowercase to ensure case-insensitive comparison
    s1 = s1.lower()
    s2 = s2.lower()
    
    # Perform lexicographical comparison
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0

# Read the input strings
s1 = input().strip()
s2 = input().strip()

# Get the result of the comparison and print it
print(compare_strings(s1, s2))
