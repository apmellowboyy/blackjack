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

#BONUES MONEY PRIZES FOR LONG TERM PLAY
def bonusBalance(wins, balance):
    if wins == 500:
        print('Dealer: You\'ve racked up 500 wins, that had to be excruciating!!!!')
        print('*You received $100,000,000 from the dealer!*')
        balance += 100000000
    elif wins == 200:
        print('\nDealer: You\'ve racked up 200 wins, here\'s a gift for your loyalty!')
        print('*You recieved $10,000,000 from the dealer!*')
        balance +=10000000
    elif wins == 100:
        print('\nDealer: You\'ve racked up 100 wins, here\'s a gift for playing!')
        print('*You recieved $1,000,000 from the dealer!*')
        balance +=1000000
    elif wins == 90:
        print('\nDealer: You\'ve racked up 90 wins, here\'s a gift for playing!')
        print('*You recieved $500,000 from the dealer!*')
        balance +=500000
    elif wins == 80:
        print('\nDealer: You\'ve racked up 80 wins, here\'s a gift for playing!')
        print('*You recieved $250,000 from the dealer!*')
        balance +=250000
    elif wins == 70:
        print('\nDealer: You\'ve racked up 70 wins, here\'s a gift for playing!')
        print('*You recieved $100,000 from the dealer!*')
        balance +=100000
    elif wins == 60:
        print('\nDealer: You\'ve racked up 60 wins, here\'s a gift for playing!')
        print('*You recieved $75,000 from the dealer!*')
        balance +=75000
    elif wins == 50:
        print('\nDealer: You\'ve racked up 50 wins, here\'s a gift for playing!')
        print('*You recieved $50,000 from the dealer!*')
        balance +=50000
    elif wins == 40:
        print('\nDealer: You\'ve racked up 40 wins, here\'s a gift for playing!')
        print('*You recieved $25,000 from the dealer!*')
        balance +=25000
    elif wins == 30:
        print('\nDealer: You\'ve racked up 30 wins, here\'s a gift for playing!')
        print('*You recieved $10,000 from the dealer!*')
        balance +=10000
    elif wins == 20:
        print('\nDealer: You\'ve racked up 20 wins, here\'s a gift for playing!')
        print('*You recieved $5,000 from the dealer!*')
        balance +=5000
    elif wins == 10:
        print('\nDealer: You\'ve racked up 10 wins, here\'s a gift for playing!')
        print('*You recieved $1,000 from the dealer!*')
        balance +=1000
    elif wins == 5:
        print('\nDealer: You\'ve racked up 5 wins, here\'s a gift for playing!')
        print('*You received $500 from the dealer!*')
        balance += 500
    return balance

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

    # YOU AND THE COMPUTER'S HAND
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
            balance = bonusBalance(wins, balance)
        # ENDING IN A DRAW IS RARE BUT MOST COMMON ON 20
        # OF COURSE NO WINS OR LOSSES BUT ADDS TO TOTAL GAMES
        elif dealer_value == cardValue(player_turn):
            print("DRAW!")
            games += 1
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
        # YOU GET A DIFFERENT RESPONSE DEPENDING ON LEAVE BALANCE
        # HIGHEST TO LOWEST ALLOWS ALL TO POTENTIALLY DISPLAY

        if balance == 0:
            print('Better luck next time!')
        elif balance >= 1000000:
            print('ONE MILLION DOLLARS!!!!!!!!!!')
        elif balance >= 100000:
            print('Time to invest and retire!')
        elif balance >= 90000:
            print('I can invest this and hit one milly!')
        elif balance >= 80000:
            print('Babe let\'s go on a cruise!')
        elif balance >= 70000:
            print('Time to start a business!')
        elif balance >= 60000:
            print('60 thousand baby!!!!')
        elif balance >= 50000:
            print('I better go play the lotto!')
        elif balance >= 40000:
            print('I can buy a house!')
        elif balance >= 30000:
            print('Walking with 30K!')
        elif balance >= 20000:
            print('Twenty Thousand!!!!')
        elif balance >= 10000:
            print('TEN....THOUSAND....DOLLARS....')
        elif balance >= 5000:
            print('WOOO-HOOO Walking away with five grand!')
        elif balance >= 1000:
            print("Let's go! Over a thousand!")
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
