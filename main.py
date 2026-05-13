from random import random, choice, choices


def random_word(words: list):
    """Choose a random word for the game"""
    if not words:
        return f'No words in the json file.'
    
    return random.choice(words).upper()


def display_game_status(secret_word, guessed_letters, unguessed_letters, number_of_attempts, attempts):

    word_for_display = ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])

    remaining = number_of_attempts - attempts

    print("\n" + '=' * 45)
    print(f' STATUS: {remaining} Attempts left | Guessed: {', '.join(guessed_letters)}')
    print('=' * 45)
    print(f'\n{12 * ' '}>>  {word_for_display}  <<\n')
    print('=' * 45)
    print(f'Wrong letters that you tried: {' '.join(unguessed_letters)}')
    print('=' * 45)


def input_validation(letter, unguessed_word, guessed_letters):
    """Validating the input if it one letter and not a letter that guessed already befor"""
    if not len(letter) == 1:
        print('The input must contain only one character.')
        return False
    
    if letter in unguessed_word or letter in guessed_letters:
        print('The letter has been tried before.')
        return False
    
    return True