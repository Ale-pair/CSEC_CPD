def correct_word(s):
    # Count uppercase and lowercase letters
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = len(s) - upper_count  # Total length minus uppercase gives lowercase count
    
    # If there are more uppercase letters, convert to uppercase, otherwise to lowercase
    if upper_count > lower_count:
        print(s.upper())
    else:
        print(s.lower())

# Input the word
s = input().strip()

# Call the function to process and print the result
correct_word(s)
