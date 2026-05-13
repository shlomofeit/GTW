from random import random, choice, choices


def random_word(words: list):
    """Choose a random word for the game"""
    if not words:
        return f'No words in the json file.'
    
    return random.choice(words).upper()