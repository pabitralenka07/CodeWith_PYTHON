import random
import string

site = input("Website: ")

password = "".join(
    random.choice(
        string.ascii_letters + string.digits
    )
    for i in range(12)
)

with open("passwords.txt", "a") as file:
    file.write(f"{site} : {password}\n")

print("Password Saved!")
print("Generated Password:", password)