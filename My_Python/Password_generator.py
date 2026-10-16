import random
import string

length = int(input("Password length: "))

chars = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = "".join(
    random.choice(chars)
    for i in range(length)
)

print("\nGenerated Password:")
print(password)
