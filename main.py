import random
import os
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dealcards():
    return random.choice(cards)
  
def calculate_score(card):
    if sum(card) == 21 and len(card)==2:
        return 0 #blackjack
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare(player_score, comp_score):
    if player_score > 21 and comp_score > 21:
        return "You went over. You lose 😤"
    if player_score == comp_score:
        return "Draw 🙃"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    
def play_game():
    print(logo)
    
    player_card = []
    comp_card = []
    is_game_over = False
    
    for i in range(2):
        player_card.append(dealcards())
        comp_card.append(dealcards())
    
    while not is_game_over:
        player_score = calculate_score(player_card)
        comp_score = calculate_score(comp_card)
        
        print(f"Your cards are {player_card} and score is: {player_score}")
        print(f"Computer first card is {comp_card[0]}")

        if (comp_score == 0 or player_score == 0 or player_score > 21) :
            is_game_over = True
        else:
            player_input = input("Enter yes if you want to deal another card otherwise no: ").lower()
            if player_input == "yes":
                player_card.append(dealcards())
            else:
                is_game_over = True
                
    while comp_score!=0 and comp_score<17:
        comp_card.append(dealcards())
        comp_score = calculate_score(comp_card)

    print(f"Your final hand is {player_card} and final score is: {player_score}")
    print(f"Computer final hand is {comp_card} and final score is: {comp_score}")
        
    print(compare(player_score, comp_score))
    
play_game() 

while input("Enter yes if you want to play again or no to exit: ").lower() == "yes":
    os.system('cls')
    play_game()
