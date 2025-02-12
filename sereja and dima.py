def game_score(n, cards):
    # Sereja and Dima's scores
    sereja_score = 0
    dima_score = 0
    
    # Pointers for the left and right ends of the card array
    left = 0
    right = n - 1
    
    # Simulate the turns: Sereja starts first
    turn = 0  # 0 for Sereja's turn, 1 for Dima's turn
    
    while left <= right:
        # Choose the larger of the two ends
        if cards[left] > cards[right]:
            chosen_card = cards[left]
            left += 1
        else:
            chosen_card = cards[right]
            right -= 1
        
        # Add the chosen card to the player's score
        if turn == 0:
            sereja_score += chosen_card
        else:
            dima_score += chosen_card
        
        # Switch turn: if it was Sereja's turn, it's now Dima's turn, and vice versa
        turn = 1 - turn
    
    # Return the final scores of both players
    return sereja_score, dima_score

# Input reading
n = int(input())  # Number of cards
cards = list(map(int, input().split()))  # List of card values

# Get the result
sereja_score, dima_score = game_score(n, cards)

# Output the result
print(sereja_score, dima_score)
