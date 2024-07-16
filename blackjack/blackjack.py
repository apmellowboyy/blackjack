#I PLAN ON SUBMITTING THIS TO MY GITHUB 

import random
import sys

# GETS YOUR NAME
enter_name = input('What is your name? ')
print('')
print(f'Welcome to blackjack, {enter_name}! Place a bet and hope you won\'t regret it!\nClosest to 21 wins, any hands over 21 will result in a bust! Keep in mind that\nKINGS, QUEENS, and JACKS equal 10, while ACES equal 1 or 11.')
print('')

# FUNCTION THAT DEALS A RANDOM CARD FOR YOU
def deal():
    # CARDS FROM 2 TO ACE
    return random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])

# FUNCTION TO CALCULATE THE VALUE OF THE HAND
def cardValue(hand):
    aces = 0
    value = 0
    # PULLING J, Q, OR K ADDS 10
    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        # PULLING AN ACE IS EITHER 1 OR 11
        elif card == 'A':
            aces += 1
            value += 11
        else:
            # INSTEAD OF 10, 1 OR 11 IT PULLS THE NUMBER SHOWN (2,3,4,5 etc.)
            value += int(card)
    # PULLING AN ACE IS 1 HERE IF HAND IS OVER 21 
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

#THIS CALCULATES WIN PERCENTAGE
def percentage(wins, games):
    if games == 0:
        return 0
    return (wins / games) * 100

# MAIN BLACKJACK GAME FUNCTION
def twentyOne(wins, losses, balance, games):
    # PROMPT PLAYER TO PLACE A BET
    while True:
        try:
            bet = int(input(f"\n{enter_name}, your balance is ${balance}. How much would you like to bet? "))
            if bet > balance:
                print("Dealer: You can\'t bet more than what you have man...")
            elif bet == 0:
                print('')
                print(f'Dealer: Are you really trying to bet $0? Get out of here!')
                print('*You have been removed by security*')
                sys.exit()
            else:
                break
        except ValueError:
            print("Dealer: Are you stupid or something?")

    #YOU AND THE COMPUTERS HAND
    player_turn = [deal(), deal()]
    computer_turn = [deal(), deal()]
    print(f"Your hand: {player_turn}")

    while True:
        action = input("Dealer: Do you want to '[h]it' or '[s]tand'? ").lower()
        print('')
        print('')
        if action == 'h':
            player_turn.append(deal())
            print(f"Your hand: {player_turn}")
            if cardValue(player_turn) > 21:
                print("YOU BUSTED! YOU LOSE!")
                losses += 1
                games += 1
                balance -= bet
                win_percentage = percentage(wins, games)
                print(f"Total Wins: {wins}")
                print(f"Total Losses: {losses}")
                print(f'\nTotal Games: {games}')
                print(f"Win percentage: {win_percentage}%")
                print(f"Balance: ${balance}")

                break
        elif action == 's':
            break

    if cardValue(player_turn) <= 21:
        dealer_value = cardValue(computer_turn)
        print(f"Computer's hand: {computer_turn} (value: {dealer_value})")
        if dealer_value > 21 or cardValue(player_turn) > dealer_value:
            print("YOU WIN!")
            wins += 1
            games += 1
            balance += bet
        #ENDING IN A DRAW IS RARE BUT MOST COMMON ON 20
        #OF COURSE NO WINS OR LOSSES BUT ADDS TO TOTAL GAMES
        elif dealer_value == cardValue(player_turn):
            print("DRAW!")
            games +=1
        else:
            print("Computer Wins!")
            losses += 1
            games += 1
            balance -= bet

        win_percentage = percentage(wins, games)
        print(f"\nTotal Wins: {wins}")
        print(f"Total Losses: {losses}")
        print(f'Total Games: {games}\n')
        print(f"Your balance is now ${balance}")
        print(f"Your win percentage is {win_percentage}%")

    # PROMPTS YOU FOR ANOTHER ROUND AND SOME EASTER EGG RESPONSES
    play_again = input("Dealer: Would you like to play another round? yes or no? ")
    if play_again == 'yes':
        return twentyOne(wins, losses, balance, games)
    elif play_again == 'you ripped me off!':
        print('Dealer: Aye bro, you just suck at giving calls.')
    elif play_again == 'rigged!':
        print('Dealer: Bro, it\'s 21. How didn\'t you win?')
    elif play_again == 'Hell yeah!':
        print('Dealer: Hell yeah!')
    elif play_again == 'no':
        print(f'\nDealer: Thank you for playing Blackjack {enter_name}, have a great day!\n')
        print(f"Total Wins: {wins}")
        print(f"Total Losses: {losses}")
        print(f'Total Games: {games}\n')
        print(f"You walked away with ${balance}")
        #YOU GET A DIFFERENT RESPONSE DEPENDING ON LEAVE BALANCE
        #HIGHEST TO LOWEST ALLOWS ALL TO POTENTIALLY DISPLAY

        if balance == 0:
            print('better luck next time!')
        elif balance >= 1000000:
            print('ONE MILLION DOLLARS!!!!!!!!!!')
        elif balance >= 100000:
            print('Time to invest and retire!')
        elif balance >= 50000:
            print('I better go play the lotto!')
        elif balance >= 20000:
            print('Twenty Thousand!!!!')
        elif balance >= 10000:
            print('TEN....THOUSAND....DOLLARS....')
        elif balance >= 5000:
            print('WOOO-HOOO Walking away with five grand!')
        elif balance >= 1000:
            print("Lets go! Over a thousand!")
        elif balance < 250:
            print(f'Leaving with less sucks!')
        else:
            print(f"Awesome! Leaving with more!")
        win_percentage = percentage(wins, games)
        print(f"Win percentage: {win_percentage}%")
        return wins, losses, balance, games

# THESE ARE THE WINS, LOSSES, TOTAL GAMES AND MONEY YOU CAN BET
wins = 0
losses = 0
balance = 250
games = 0
wins, losses, balance, games = twentyOne(wins, losses, balance, games)
