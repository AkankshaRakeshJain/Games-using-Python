import random
import os

# creating function
def calculate(card_value):
    non_ace_card = [card for card in card_value if card != 'A']
    ace_card = [card for card in card_value if card == 'A']
    sum = 0
    for card in non_ace_card:
        if card in 'JQK':
            sum += 10
        else:
            sum += int(card)
    for card in ace_card:
        if sum <= 10:
            sum += 11
        else:
            sum += 1
    return sum


while True:
    cards = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
    ]
    random.shuffle(cards)
    player = []
    dealer = []
    player.append(cards.pop())
    dealer.append(cards.pop())
    player.append(cards.pop())
    dealer.append(cards.pop())

    standing = False
    blackjack = True

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        dealer_score = calculate(dealer)
        player_score = calculate(player)

        if standing:
            print('Dealer cards:   [{}] [{}]'.format(
                ']['.join(dealer), dealer_score))
        else:
            print('Dealer Cards: [{}][?]'.format(dealer[0]))

        print('Your cards:   [{}] [{}]'.format(
            ']['.join(player), player_score))
        print('')

        if standing:
            if dealer_score > 21:
                print("Dealer busted, you win")
            elif dealer_score == player_score:
                print('Draw, nobody win')
            elif player_score > dealer_score:
                print('You win!')
            else:
                print('You lose')
            print('')
            input('Play again? Hit enter to continue')
            break

        if blackjack and player_score == 21:
            print('Blackjack!')
            input('Play again? Hit enter to continue')
            break

        if player_score > 21:
            print('You busted')
            input('Play again? Hit enter to continue')
            break

        print('Your choice:')
        print('(1)Hit \n(2)Stand')
        choice = input()

        blackjack = False
        if choice == '1':
            player.append(cards.pop())
        elif choice == '2':
            standing = True
            while calculate(dealer) <= 16:
                dealer.append(cards.pop())

