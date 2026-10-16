import random

columns = [
    "customerid",
    "orderdate",
    "totalamount",
    "status"
]

word = random.choice(columns)

guessed = set()
attempts = 8

while attempts > 0:

    display = "".join(
        c if c in guessed else "_"
        for c in word
    )

    print(f"\nWord: {display}")
    print(f"Attempts left: {attempts}")

    guess = input("Guess letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.add(guess)

    if guess not in word:
        attempts -= 1
        print("Not in the word.")

    if all(c in guessed for c in word):
        print(f"\nYou win! The word was '{word}'.")
        break

else:
    print(f"\nOut of attempts! The word was '{word}'.")
    