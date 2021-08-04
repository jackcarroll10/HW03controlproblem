print('G U E S S I N G   G A M E ')
def guessing_game():
    answer = 8
    guess = 0
    i = 0
    while guess != 8:
        guess = int(input('Guess an integer from 1-20'))
        i += 1
        if guess > 8:
            print('Try a lower number')
        if guess < 8:
            print('Try a higher number')
    print('You guessed the number!')
    print('It took you', i, 'guesses')

guessing_game()