import random

# Define the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

# Function to shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)
# Function to deal a hand of cards
def deal_hand(deck, num_cards=5):
    return [deck.pop() for _ in range(num_cards)]

# Function to evaluate the poker hand and return its rank
def evaluate_hand(hand):
    # You can implement more sophisticated hand evaluation logic here
    # This simple version just checks for pairs
    ranks_count = {}
    for card in hand:
        rank = card['rank']
        if rank in ranks_count:
            ranks_count[rank] += 1
        else:
            ranks_count[rank] = 1

    max_count = max(ranks_count.values())
    if max_count == 2:
        return "One Pair"
    elif max_count == 3:
        return "Three of a Kind"
    elif max_count == 4:
        return "Four of a Kind"
    else:
        return "High Card"

# Function to get the user's choice for discarding cards
def get_discard_choice(player_hand):
    print("Your current hand:")
    for i, card in enumerate(player_hand):
        print(f"{i + 1}: {card['rank']} of {card['suit']}")

    discard_indices = input("Enter the numbers of the cards you want to discard (e.g., 1 3 4): ").split()
    discard_indices = [int(index) - 1 for index in discard_indices]

    discarded_cards = []
    for index in discard_indices:
        if 0 <= index < len(player_hand):
            discarded_cards.append(player_hand.pop(index))

    return discarded_cards

# Function to play a round of poker
def play_poker():
    shuffle_deck(deck)
    player_hand = deal_hand(deck)
    computer_hand = deal_hand(deck)

    player_chips = 100  # Initial number of chips for the player
    bet = 0

    while True:
        print(f"Your current chips: {player_chips}")
        try:
            bet = int(input("Enter your bet (1 to 10 chips): "))
            if 1 <= bet <= 10 and bet <= player_chips:
                break
            else:
                print("Invalid bet. Please enter a valid bet.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")

    print("Your hand:")
    for card in player_hand:
        print(f"{card['rank']} of {card['suit']}")

    discarded_cards = get_discard_choice(player_hand)
    player_hand += deal_hand(deck, len(discarded_cards))

    player_hand_value = evaluate_hand(player_hand)
    print(f"Your hand: {player_hand_value}\n")

    print("Computer's hand:")
    for card in computer_hand:
        print("Face Down Card")

    input("\nPress Enter to reveal the computer's hand...")

    print("\nComputer's hand:")
    for card in computer_hand:
        print(f"{card['rank']} of {card['suit']}")

    computer_hand_value = evaluate_hand(computer_hand)
    print(f"Computer's hand: {computer_hand_value}\n")

    if player_hand_value > computer_hand_value:
        print("You win this round!")
        player_chips += bet
    elif player_hand_value < computer_hand_value:
        print("Computer wins this round!")
        player_chips -= bet
    else:
        print("It's a tie this round!")

    return player_chips

# Main game loop
while True:
    player_chips = play_poker()
    if player_chips <= 0:
        print("You've run out of chips. Game over!")
        break
    play_again = input("\nDo you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        break
