import random
lst = ['sound','fun','noise','happy','sleep','calculator','program']
word = random.choice(lst)
print('The word contain',len(word) , 'letters')

# creating two list
correct_guess = ['_'] * len(word)
incorrect_guess = []

# defining functions
def parts(x):
    if x == 0:
        print('------')
        print('|    |')
        print('|     ')
        print('|     ')
        print('|     ')
        print('|     ')
        print('===============')
    if x == 1:
        print('------')
        print('|    |')
        print('|    O')
        print('|     ')
        print('|     ')
        print('|     ')
        print('===============')
    if x == 2:
        print('------')
        print('|    |')
        print('|    O')
        print('|   -|')
        print('|     ')
        print('|     ')
        print('===============')
    if x == 3:
        print('------')
        print('|    |')
        print('|    O')
        print('|   -|-')
        print('|    | ')
        print('|     ')
        print('===============')
    if x == 4:
        print('------')
        print('|    |')
        print('|    O')
        print('|   -|-')
        print('|    | ')
        print('|   / ')
        print('===============')
    if x == 5:
        print('------')
        print('|    |')
        print('|    O')
        print('|   -|-')
        print('|    | ')
        print('|   / \\')
        print('===============')


def update():
    for i in correct_guess:
        print(i,end=' ')
    print()

def main():
    while True:
        user_input = input('Guess a letter: ')
        if user_input in word:
            index = 0
            for i in word:
                if user_input == i:
                    correct_guess[index] = user_input #add userinput value at correct positon
                index += 1
            update()
        else:
            if user_input not in incorrect_guess:
                incorrect_guess.append(user_input)
                parts(len(incorrect_guess))
            else:
                print('You already guessed it')
            print(incorrect_guess)

        if len(incorrect_guess) >4:
            print('Game over')
            print('System picked:',word)
            break
        if '_' not in correct_guess:
            print('You win')
            break


if __name__ == "__main__":
    update()
    parts(len(incorrect_guess))
    main()
