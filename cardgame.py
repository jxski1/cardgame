# Jaskirat Singh
# Tricksy Battle
# Rules:
# You use a regular deck of cards without Kings (so 48 cards).
# Both players get 8 cards each to start.
# Each round, both players play 1 card.
# The first player “leads” by playing any card; the other player must follow the same suit if they can.
# Whoever plays the highest card in the lead suit wins the round and earns 1 point.
# After each round:
# A random card from the deck is flipped over for both players to see (just for info).
# The winner of the round leads the next round.
# When both players get down to 4 cards, they each get 4 more cards (this happens twice).
# The game ends after 16 rounds (16 points max), OR early if someone hits 9 points and the other player has at least 1 point (because the other person can’t catch up).
# Special rule: If someone wins 16-0, they “shoot the moon” and instantly win with 17 points.


import random

# deck of cards (without kings)
deck = [
    '2H', '2D', '2C', '2S',
    '3H', '3D', '3C', '3S',
    '4H', '4D', '4C', '4S',
    '5H', '5D', '5C', '5S',
    '6H', '6D', '6C', '6S',
    '7H', '7D', '7C', '7S',
    '8H', '8D', '8C', '8S',
    '9H', '9D', '9C', '9S',
    '10H', '10D', '10C', '10S',
    'JH', 'JD', 'JC', 'JS',
    'QH', 'QD', 'QC', 'QS',
    'AH', 'AD', 'AC', 'AS']

# shuffle the deck
random.shuffle(deck)

# deal cards to players
player1 = deck[:8]
player2 = deck[8:16]
deck = deck[16:]

print("Player 1 hand:", player1_hand)
print("Player 2 hand:", player2_hand)
print("Remaining deck:", remaining_deck)

# track scores
player1_score = 0
player2_score = 0

# simple function to get card value (ignores suits)
def card_value(card):
    rank = card[:-1] 
    if rank == 'J':
        return 11
    elif rank == 'Q':
        return 12
    elif rank == 'A':
        return 14
    else:
        return int(rank)

# function to play a round
def play_round(p1_hand, p2_hand, leader):
    print("\n--- New Round ---")

    # leader chooses card first
    if leader == 1:
        p1_card = p1_hand.pop(0)
        p2_card = p2_hand.pop(0)
    else:
        p2_card = p2_hand.pop(0)
        p1_card = p1_hand.pop(0)

    print(f"Player 1 plays {p1_card}")
    print(f"Player 2 plays {p2_card}")

    # compare values
    if card_value(p1_card) > card_value(p2_card):
        print("Player 1 wins the round!")
        return 1
    elif card_value(p2_card) > card_value(p1_card):
        print("Player 2 wins the round!")
        return 2
    else:
        print("It's a tie!")
        return 0  # tie

# example of playing 1 round (player 1 starts)
leader = 1
winner = play_round(player1_hand, player2_hand, leader)

# update score
if winner == 1:
    player1_score += 1
    leader = 1
elif winner == 2:
    player2_score += 1
    leader = 2

print(f"Scores -> Player 1: {player1_score} | Player 2: {player2_score}")