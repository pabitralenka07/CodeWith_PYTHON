import random


def roll_dice(sides=6):
    return random.randint(1, sides)


rounds = int(input("How many rounds? "))
target = int(input("Target score to reach: "))

total = 0
history = []
round_num = 0

while total < target and round_num < rounds:

    roll = roll_dice()

    total += roll
    round_num += 1

    history.append(roll)

    print(f"Round {round_num}: rolled {roll}, total = {total}")


if total >= target:
    print(
        f"\nYou reached {total} "
        f"in {round_num} rounds!"
    )
else:
    print(
        f"\nOut of rounds! "
        f"Final score: {total}"
    )

print(f"Rolls: {history}")
