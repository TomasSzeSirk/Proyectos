"""Generates a random password with the specified length."""
from string import ascii_letters, digits, punctuation
from secrets import choice
from sys import argv

HELP = '''Usage: python3 password_generator.py [options] [length]\n
Generates a random password with the specified length.\n
Arguments:\n
Length: (Optional) The length of the password to generate. Must be a number greater than 0. If not given, the length will be 8 characters\n
-d <number of repetitions>: (Optional) Allows a maximum quantity of repeating characters in the password. The value is the number of times a character can repeat.\n
-h, --help: Shows this help message.\n
Examples:\n
password_generator.py 12
Generates a random password with 12 characters.\n
password_generator.py -d 2 12
Generates a random password with 12 characters, allowing each character to repeat up to 2 times.\n
password_generator.py
Generates a random password with 8 characters.\n'''

def password_generator(times_can_be_repeated: int,
                       do_not_repeat_characters: bool = False, lentgh: int = 8) -> str:
    """Generates a random password with the specified length."""
    password = ""
    alphabet = ascii_letters + digits + punctuation + " "

    for _ in range(lentgh):
        character = choice(alphabet)

        if do_not_repeat_characters and password.count(character) >= times_can_be_repeated:
            alphabet = alphabet.replace(character, "")
            character = choice(alphabet)

        password += character
    return password

def verify_length(length: int, max_repetitions: int = 0) -> bool:
    """Verify if the length is valid."""
    return length > 0 and length < max_repetitions*95 if max_repetitions > 0 else length > 0

def read_arguments(arguments) -> None:
    """Read the arguments and generate the password."""
    try:
        if arguments[1] == "-h" or arguments[1] == "--help":
            print(HELP)
        elif arguments[1] == "-d":
            try:
                if not verify_length(int(arguments[3]), int(arguments[2])):
                    print("Error: Invalid maximum length.")
                    return
                print(f"Password: {password_generator(int(arguments[2]), True, int(arguments[3]))}")

            except IndexError:
                if not verify_length(8,int(arguments[2])):
                    print("Error: Invalid argument. The length must be greater than 0\n")
                    return

                print(f"Password: {password_generator(int(arguments[2]), True)}")
        else:
            if not verify_length(int(arguments[1])):
                print("Invalid argument. The length must be greater than 0\n")
                return

            print(f"Password: {password_generator(-1, lentgh = int(arguments[1]))}")
    except IndexError:
        print(f"Password: {password_generator(-1)}")

def is_not_valid_repetition_arguments():
    """Verify if the arguments for the repetition are valid."""
    return ((len(argv) > 4 or len(argv) < 3) and argv[1] == "-d")


def main():
    """Main function of the script"""
    try:
        try:
            if is_not_valid_repetition_arguments() or (len(argv) > 2 and argv[1] != "-d"):
                print("Error: Invalid number of arguments. You must provide only one argument\n")
                return

            read_arguments(argv)
        except IndexError:
            read_arguments(argv)

    except ValueError:
        print("Error: Invalid argument, You must provide a number as argument\n")
main()
