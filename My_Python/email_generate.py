import random
import string

def generate_email():
    username = "".join(
        random.choices(
            string.ascii_lowercase + string.digits,
            k=8
        )
    )

    domains = [
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "example.com"
    ]

    domain = random.choice(domains)

    return f"{username}@{domain}"

print(generate_email())
