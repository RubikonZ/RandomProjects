from random import randint


def main():
    randomly_chosen_number = randint(1, 101)
    correct = False
    answer = ''
    guesses = 0

    while not correct:
        player_guess = int(input('Choose number between 1 and 100: '))
        diff = abs(randomly_chosen_number - player_guess)
        guesses += 1
        if player_guess < randomly_chosen_number:
            print('Wrong. It is higher')
            if diff > 15:
                answer = 'pretty far'
            elif diff < 5:
                answer = 'very close'
            print(f'You are {answer}')
        elif player_guess > randomly_chosen_number:
            print('Wrong. It is lower')
            if diff > 15:
                answer = 'pretty far'
            elif diff < 5:
                answer = 'very close'
            print(f'You are {answer}')
        else:
            print(f'Correct! This took you {guesses} guesses')
            correct = True

    play_again = input('Wanna play again? Y/N: ')
    if str(play_again).lower() == 'y':
        main()
    elif str(play_again).lower() == 'n':
        print('Have a nice day.')
        return

if __name__=='__main__':
    main()