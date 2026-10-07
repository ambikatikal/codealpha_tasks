import random

# List of words for the game
words = ["python", "computer", "programming", "developer", "coding"]

# Select a random word from the list
secret_word = random.choice(words)

# Store the letters guessed by the player
guessed_letters = []

# Track the number of incorrect guesses
incorrect_guesses = 0
max_guesses = 6

# Display welcome message
print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Continue the game until the player reaches the maximum wrong guesses
while incorrect_guesses < max_guesses:

    display_word = ""

    # Display guessed letters and underscores for remaining letters
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

    # Get a letter from the player
    guess = input("Guess a letter: ").lower()

    # Check if the input is exactly one letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the new guess to the guessed letters
    guessed_letters.append(guess)

    # Check whether the guessed letter is in the secret word
    if guess in secret_word:
        print("Good guess! 🎉")
    else:
        incorrect_guesses += 1
        print("Wrong guess! ❌")

    # Check if the player has guessed the complete word
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! 🎉 You guessed the word!")
        break

# Display the answer if the player uses all six incorrect guesses
if incorrect_guesses == max_guesses:
    print("\nGame Over! ❌")
    print("The word was:", secret_word)