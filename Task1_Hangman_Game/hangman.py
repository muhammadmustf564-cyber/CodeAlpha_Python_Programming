import random

words = ["python", "network", "security", "computer", "program"]

word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("================================")
print("       HANGMAN GAME")
print("================================")

while incorrect_guesses < max_incorrect_guesses:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses)
    print("Guessed letters:", guessed_letters)

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame Over!")
    print("The word was:", word)