def minimum_horseshoes_to_buy(s1, s2, s3, s4):
    # Put the horseshoes into a set to count unique colors
    unique_colors = {s1, s2, s3, s4}
    
    # The number of horseshoes Valera needs to buy is the difference between 4 and the number of unique colors
    return 4 - len(unique_colors)

# Input
s1, s2, s3, s4 = map(int, input().split())

# Output
print(minimum_horseshoes_to_buy(s1, s2, s3, s4))
