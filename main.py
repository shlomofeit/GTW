from random import random, choice, choices
from time import sleep


guessed_letters = []
unguessed_letters = []
number_of_attempts = 15

def random_word(words: list):
    """Choose a random word for the game"""
    if not words:
        return f'No words in the json file.'
    
    return list(random.choice(words).upper())


def display_game_status(secret_word, guessed_letters, unguessed_letters, number_of_attempts, attempts):

    word_for_display = ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])

    remaining = number_of_attempts - attempts

    print("\n" + '=' * 45)
    print(f' STATUS: {remaining} Attempts left | Guessed: {', '.join(guessed_letters)}')
    print('=' * 45)
    print(f'\n{12 * ' '}>>  {word_for_display}  <<\n')
    print('=' * 45)
    print(f'Wrong letters that you tried: {' '.join(unguessed_letters)}')
    print('=' * 45, '\n\n\n')
    sleep(0.5)


def input_validation(letter, unguessed_word, guessed_letters):
    """Validating the input if it one letter and not a letter that guessed already befor"""
    if not len(letter) == 1:
        print('The input must contain only one character.')
        return False
    
    if letter in unguessed_word or letter in guessed_letters:
        print('The letter has been tried before.')
        return False
    
    return True


def get_user_input(unguessed_word, guessed_word):
    """Manage the dialog with the user"""
    while not input_validation:
        user_input = input('Enter your guess:\n>>> ').upper()
        input_validation(user_input, unguessed_word, guessed_word)

    return True


def game_logic(letter, word):
    """check if the letter are correct"""
    if letter not in word:
        unguessed_letters.append(letter)
        return False
    
    guessed_letters.append(letter)
    return True


def win_check(guessed_letters, word):
    """Check if the game is done"""
    if all(letter in guessed_letters for letter in word):
        return True
    
    return False


def print_menu():
    print('\n' + '=' * 30)
    print(f'{'MAIN MENU':^30}')
    print('=' * 30)
    print('1. Start new game')
    print('2. View game history')
    print('3. Exit')
    print('=' * 30)

    while True:
        choice = input('Select an option (1-3):\n>>> ')
        if choice in '123':
            sleep(0.5)
            break

        else:
            sleep(0.5)
            print('\nChoose only 1-3.\n')
            sleep(0.5)

    return choice

def main():
    pass