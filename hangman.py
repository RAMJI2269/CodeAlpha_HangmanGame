import random

words = ["PYTHON", "APPLE", "COMPUTER", "PROGRAM", "CODING"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0

print("Welcome to Hangman!")

while wrong_guesses < 6:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won! 🎉")
        break
    guess = input("Guess a letter: ").strip().upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Incorrect guesses:", wrong_guesses, "/ 6")

if wrong_guesses == 6:
    print("\nGame over! The word was:", word)