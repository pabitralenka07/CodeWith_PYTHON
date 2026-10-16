import random

choices = ["rock", "paper", "scissors"]

player = input("Choose rock, paper or scissors: ").lower()

computer = random.choice(choices)

print("Computer chose:", computer)

if player == computer:
    print(f"It's a tie! Both chose {player}.")

elif (
    (player == "rock" and computer == "scissors")
    or (player == "paper" and computer == "rock")
    or (player == "scissors" and computer == "paper")
):
    print(f"You win! {player} beats {computer}.")

elif player in choices:
    print(f"Computer wins! {computer} beats {player}.")

else:
    print("Invalid choice! Please choose rock, paper or scissors.")
    