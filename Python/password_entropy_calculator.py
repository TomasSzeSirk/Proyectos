"""Calculate the entropy of a password based on the characters it contains"""
from math import log2
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from sys import argv

HELP = '''Usage: python3 password_entropy_calculator.py [options] [password]

Options:
    -h, --help: Shows this help message.

Arguments:
    password: The password for which to calculate the entropy.

Example:
    password_entropy_calculator.py mySecureP@ssw0rd
'''

def calculate_range(password: str) -> int:
    """Calculate the range of a password based on the characters it contains"""
    password_range = 0
    password_range += len(punctuation) if any(char in punctuation for char in password) else 0
    password_range += 10 if any(char in digits for char in password) else 0
    password_range += 26 if any(char in ascii_lowercase for char in password) else 0
    password_range += 26 if any(char in ascii_uppercase for char in password) else 0

    return password_range

def calculate_entropy(password: str):
    """Calculate the entropy of a password using the formula: log2(Range^Length)"""
    password_range = calculate_range(password)
    entropy = log2(password_range ** len(password))
    return entropy

def categorize_entropy(entropy: float) -> str:
    """Categorize the entropy of a password based on its value"""
    if entropy < 28:
        return "Very Weak"
    elif entropy < 35:
        return "Weak"
    elif entropy < 59:
        return "Reasonable"
    elif entropy < 127:
        return "Strong"
    else:
        return "Very Strong"

def main():
    """Main function of the script"""
    if len(argv) != 2:
        print("Error: Invalid number of arguments. You must provide a password as argument\n")
        return

    if argv[1] == "-h" or argv[1] == "--help":
        print(HELP)
        return

    password = argv[1]
    print(f"Password: {password}")
    entropy = calculate_entropy(password)
    print(f"Entropy: {entropy}")
    print(f"{categorize_entropy(entropy)} Password")
main()
