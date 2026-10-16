import random
import string


def generate_password(length, use_upper, use_lower, use_digits, use_special):

    characters = ""

    if use_upper:
        characters += string.ascii_uppercase

    if use_lower:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type!"

    password = "".join(
        random.choice(characters)
        for i in range(length)
    )

    return password


def main():

    print("===== PASSWORD GENERATOR =====")

    length = int(input("Enter password length: "))

    use_upper = input(
        "Include uppercase letters? (y/n): "
    ).lower() == "y"

    use_lower = input(
        "Include lowercase letters? (y/n): "
    ).lower() == "y"

    use_digits = input(
        "Include digits? (y/n): "
    ).lower() == "y"

    use_special = input(
        "Include special characters? (y/n): "
    ).lower() == "y"

    password = generate_password(
        length,
        use_upper,
        use_lower,
        use_digits,
        use_special
    )

    print("\nYour Strong Password:")
    print(password)


if __name__ == "__main__":
    main()
    
    