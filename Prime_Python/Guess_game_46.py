
secret = 7

while True:
    guess = int(input("Guess the number: "))

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")
        
        break
