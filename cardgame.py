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
import time

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

print("Player 1 hand:", player1)
print("Player 2 hand:", player2)
print("Remaining deck:", deck)


# ~~~~~~~~~~~~ START OF SUGGESTION ~~~~~~~~~~~~ #
# - concept: Changed countdown logic into a 'countdown()' function for easier callback

# - I like the countdown concept a lot, however, you could make this more efficient
# - while also practicing better "coding principle" by doing this instead


# - adds a countdown before the game begins for added immersion and realism in gameplay loop
# def countdown():
    # print("\nStarting Tricksy Battle in...")
    # for num in ["3...", "2...", "1... Go!\n"]
        # print(num)
        # time.sleep(1.0)

# - from there you can call the function as such:
# ~~~~~~~~~~ countdown()


# ~~~~~~~~~~~~ END OF SUGGESTION ~~~~~~~~~~~~ #

print("\nStarting Tricksy Battle in...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1... Go!\n")

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
winner = play_round(player1, player2, leader)

# update score
if winner == 1:
    player1_score += 1
    leader = 1
elif winner == 2:
    player2_score += 1
    leader = 2

print(f"Scores -> Player 1: {player1_score} | Player 2: {player2_score}")

# play full game (8 rounds)
for round_num in range(16):
    # flip a card from remaining deck
    if len(deck) > 0:
        flipped_card = deck.pop(0)
        print(f"\nFlipped card from deck: {flipped_card}")
    else:
        print("\nNo more cards to flip.")

    # play round
round_start = time.time()
winner = play_round(player1, player2, leader)
round_end = time.time()
duration = round_end - round_start
print(f"⏲️ Round took {round(duration, 2)} seconds.")

    # update scores and leader
if winner == 1:
    player1_score += 1
    leader = 1
elif winner == 2:
    player2_score += 1
    leader = 2
    # no change of leader on tie

    print(f"Scores -> Player 1: {player1_score} | Player 2: {player2_score}")

# final results
print("\n--- Game Over ---")
if player1_score > player2_score:
    print("Player 1 wins the game!")
elif player2_score > player1_score:
    print("Player 2 wins the game!")
else:
    print("The game is a tie!")
