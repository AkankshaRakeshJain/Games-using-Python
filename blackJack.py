import random
import os


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


'''
import random
import os


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
    player.append(cards.pop())
    dealer.append(cards.pop())
    dealer.append(cards.pop())

    first_hand = True
    standing = False

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    player_score = calculate(player)
    dealer_score = calculate(dealer)

    if standing:
        print('Dealer Cards: [{}] ({})'.format(
            ']['.join(dealer), dealer_score))
    else:
        print('Dealer Cards: [{}][?]'.format(dealer[0]))

    print('Your cards:   [{}] [{}]'.format(
        ']['.join(player), player_score))
    print('')

    if standing:
        if dealer_score > 21:
            print('Dealer busted, you win!')
        elif player_score == dealer_score:
            print('Push, nobody wins')
        elif player_score > dealer_score:
            print('You beat the dealer, you win!')
        else:
            print('You lose')

        print('')
        input('Play again? Hit enter to continue')
        break

    if first_hand and player_score == 21:
        print('Blackjack! Nice!')
        print('')
        input('Play again? Hit enter to continue')
        break

    if player_score > 21:
        print('You busted!')
        print('')
        input('Play again? Hit enter to continue')
        break

    print('Enter your choice:')
    print('(1) Hit \n(2) Stand')

    choice = input()
    print('')

    first_hand = False  #***********
    if choice == '1':
        player.append(cards.pop())
    elif choice == '2':
        standing = True
        while calc_hand(dealer) <= 16:
            dealer.append(cards.pop())
'''

'''import random
def check(card_value):
    if cards[0:1] == 'J' or cards[0:1] == 'Q' or cards[0:1] == 'K':
        card_value += 10
    elif cards[0:1] == 'A':
        card_value += 1
    return card_value
cards = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
]
random.shuffle(cards)
dealer = []
player = []
value = '0'
while value == '18':
    user = input('stop or hit?')
    if user == 'hit':
        x = cards[0:1]  # you can use pop()
        if x == 'J' or x == 'Q' or x == 'K' or x == 'A':
            value += check(x)  # int
        else:
            value += str(x)
        player.append(cards[0:1])
    elif user == 'stop':
        print('Stop')
        pass
if value == '21':
    print('Won and total profit of 150%')
# elif value == dealer:
    # print('No loss no profit')
elif value > '21':
    print('greater')
elif value < '21':
    print('Less than', value)
'''
