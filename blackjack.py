import random


def deal_card():
    """returns a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Checks whether the user or computer has a blackjack and returns the sum"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    

    if sum(cards) > 21 and 11 in cards :
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "DRAW!"
    elif c_score == 0:
        return "LOSE, opponent has a BLACKJACK!"
    elif u_score == 0:
        return "WIN with a BLACKJACK"
    elif u_score > 21:
        return "You went over, you LOSE!"
    elif u_score > c_score :
        return "you WIN!"
    else :
        return "You LOSE!"

def play_game():
    computer_cards = []
    user_cards = []

    #taking an empty list and adding 2 random cards 
    for _ in range(2):
        user_cards.append(deal_card)
        computer_cards.append(deal_card)

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")

        computer_score = calculate_score(computer_cards)
        print(f"Computer's first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21 :
            is_game_over = True
        else:
            user_deals =input("type 'y' to get another card, type 'n' to pass: ")
        if user_deals == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, finalscore: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you wanna play a game of BLACKJACK? Type 'y' or 'n'") == "y":
    print("\n" * 30)
    play_game()
    

