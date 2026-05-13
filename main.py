from random import choice
from time import sleep

words = [
    "PYTHON", "PROGRAMMING", "DEVELOPER", "ALGORITHM", 
    "BOOLEAN", "VARIABLE", "FUNCTION", "DATABASE", 
    "NETWORK", "SECURITY", "ASSEMBLY", "CYBER", 
    "COFFEE", "ISRAEL", "SUCCESS", "CHALLENGE"
]

def random_word(words: list):
    """Choose a random word for the game"""
    if not words:
        return f'No words in the json file.'
    
    return list(choice(words).upper())


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
    return remaining


def input_validation(letter, unguessed_word, guessed_letters):
    """Validating the input if it one letter and not a letter that guessed already befor"""
    if not letter.isalpha():
        print('The input must contain letters only.')
        return False
    
    if len(letter) != 1:
        print('The input must contain only one character.')
        return False
    
    if letter in unguessed_word or letter in guessed_letters:
        print('The letter has been tried before.')
        return False
    
    
    return True


def get_user_input(unguessed_word, guessed_word):
    """Manage the dialog with the user"""
    input_validation_val = ''
    while not input_validation_val:
        user_input = input('Enter your guess:\n>>> ').upper()
        input_validation_val = input_validation(user_input, unguessed_word, guessed_word)

    return user_input


def game_logic(letter, word, unguessed_letters, guessed_letters):
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
        if choice in ('1', '2', '3'):
            sleep(0.5)
            break

        else:
            sleep(0.5)
            print('\nChoose only 1-3.\n')
            sleep(0.5)

    return choice

def main():
    """The main function of the game"""
    
    sleep(0.5)
    print("\n" + "╔" + "═"*43 + "╗")
    print("║" + " "*43 + "║")
    print("║" + "   WELCOME TO THE ULTIMATE GUESSING GAME   " + "║")
    print("║" + " "*43 + "║")
    print("╚" + "═"*43 + "╝")
    sleep(0.5)
    print(f"{'Prepare your brain...':^45}")

    while True:
        user_choice = print_menu()
        if user_choice == '2':
            print('Coming soon...')

        elif user_choice == '3':
            print('Bye<>Bye')
            break

        elif user_choice == '1':
            number_of_attempts_val = 0
            attempts = 15
            guessed_letters = []
            unguessed_letters = []
            word = random_word(words)
            while True:
                remaining = display_game_status(word, guessed_letters, unguessed_letters, attempts, number_of_attempts_val)
                user_input = get_user_input(unguessed_letters, guessed_letters)

                if game_logic(user_input, word, unguessed_letters, guessed_letters):
                    sleep(0.5)
                    print('\nNice one! You found a letter.\n')
                    sleep(1.5)
                else:
                    sleep(0.5)
                    print('\nOops! That letter is not there.\n')
                    number_of_attempts_val += 1
                    sleep(1.5)

                if win_check(guessed_letters, word):
                    sleep(0.5)
                    print('\n\n\nCongratulations! You are the winner!\n\n\n')
                    sleep(1)
                    display_game_status(word, guessed_letters, unguessed_letters, attempts, number_of_attempts_val)
                    sleep(2)
                    break

                if number_of_attempts_val >= attempts:
                    sleep(0.5)
                    print('\n\nGame Over! You ran out of guesses.\n\n')
                    sleep(0.5)
                    break
        # break
            

main()