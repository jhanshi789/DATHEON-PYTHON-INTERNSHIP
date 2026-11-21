import random

# List of secret words
words = ["PYTHON", "COMPUTER", "PROGRAM", "DATABASE",
         "KEYBOARD", "INTERNET", "SOFTWARE"]

# Hangman stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

def play_game():

    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\nWELCOME TO HANGMAN GAME!")

    while wrong_guesses < max_attempts:

        print(hangman_stages[wrong_guesses])

        # Display hidden word
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Guessed letters:", guessed_letters)
        print("Attempts left:", max_attempts - wrong_guesses)

        if all(letter in guessed_letters
               for letter in secret_word):
            print("\nCongratulations! You won!")
            return

        guess = input("\nGuess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one alphabet letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            wrong_guesses += 1

    print(hangman_stages[wrong_guesses])
    print("\nGame Over!")
    print("The correct word was:", secret_word)


# Start game
while True:
    play_game()

    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for playing!")
        break