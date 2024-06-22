from secrets import choice
from sys import argv
from os import system, name

HELP = '''
Usage: python3 word_complicator.py [WORD]

This program takes a word and complicates it to generate a password.

Arguments:
    WORD    The word you want to complicate. It is recommended that the word is at least 8 characters long.

Options:
    -h, --help  Show this help message
'''
DICTIONARY = {"a": ["4", "@", "A", "a"], "b": ["8", "B", "b"], "c": ["(", "C", "c"], "e": ["3", "E", "e"], "g": ["9", "G", "g"], 
              "i": ["1", "!", "I", "i", "|"], "l": ["1", "!", "l", "L", "|"], "o": ["0", "O", "o"], "s": ["5", "$", "S", "s", "§"], 
              "t": ["7", "T", "t"], "y": ["&", "Y", "y"] ,"z": ["2", "5", "Z", "z"]
            }

def word_complicator(word: str) -> str:
    for character in word:
        if character.lower() in DICTIONARY:
            word = word.replace(character, choice(DICTIONARY[character]), 1)
        else:
            word = word.replace(character, choice([character.upper(), character.lower()]), 1)
    
    return word

def clear():
 
    if name == 'nt':
        system('cls')
 
    else:
        system('clear')

def main(argv: list = argv):
    if len(argv) != 2:
        print("Error: Invalid number of arguments. You must provide only one argument\n")
        return
    
    if argv[1] == "-h" or argv[1] == "--help":
        print(HELP)
        return
    
    clear()

    if len(argv[1]) < 8:
        print("Recommended: The length of the password should be more than 8 characters")
    
    not_happy_with_modifications = True

    while not_happy_with_modifications:
        print(f"Modified Word: {word_complicator(argv[1])}")
        not_happy_with_modifications = input("Are you happy with the modifications? [y/n]: ").lower() != "y" 
        clear() if not_happy_with_modifications else None

main()