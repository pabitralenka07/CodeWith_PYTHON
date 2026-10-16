import time
import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = input("Set Password: ")

print("\nAccessing Database.....\n")

guess = ""

while guess != password:
    guess = ""

    for i in range(len(password)):
        guess += random.choice(chars)

    print("Trying....!", guess)
    time.sleep(0.01)

print("\nPASSWORD CRACKED:", password)
