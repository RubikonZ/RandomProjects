

hidden_word = 'lettuce'
guessed_letters_list = []
available_guesses = 6

def game_process(hidden_word, available_guesses):
    counter = 0
    guessing_game_is_running = True

    while guessing_game_is_running:
        guessed_letter = input('\nGuess a letter: ').lower()
        if guessed_letter.isalpha() and len(guessed_letter) == 1 and guessed_letter not in guessed_letters_list:
            guessed_letters_list.append(guessed_letter)
        elif guessed_letter in guessed_letters_list:
            print(f'You have already guessed this letter, try any other')
            continue
        else:
            print('Wrong input, try again')
            continue
        counter += 1

        remaining_letters = []
        for letter in hidden_word:
            if letter in guessed_letters_list:
                remaining_letters.append(letter)
            else:
                remaining_letters.append('_')
        print(*remaining_letters)
        print(f'Guesses left: {available_guesses - counter}')

        if '_' not in remaining_letters:
            print(f'you finished the game in {counter} guesses with {available_guesses - counter}')
            guessing_game_is_running = False

        if (available_guesses - counter) <= 0:
            print(f'you have no more guesses, word was "{hidden_word}"')
            guessing_game_is_running = False


if __name__ == '__main__':
    game_process(hidden_word, available_guesses)
    # if set(guessed_letters_list, hidden_word):