import random

words = ["python", "coding", "shadowfox", "intern", "developer"]

word = random.choice(words)
guessed = []
tries = 6

while tries > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print(display)

    if display == word:
        print("You won!")
        break

    guess = input("Enter a letter: ")

    if guess in guessed:
        print("Already guessed")
        continue

    guessed.append(guess)

    if guess not in word:
        tries -= 1
        print("Wrong guess. Tries left:", tries)

if tries == 0:
    print("You lost. Word was:", word)
