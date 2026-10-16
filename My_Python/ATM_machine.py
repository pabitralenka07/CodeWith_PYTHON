import random
import time
from faker import Faker


def run_atm():

    fake = Faker("en_PK")

    account_holder = fake.name()
    account_number = random.randint(10000, 99999)
    balance = random.randint(1000, 50000)

    print("========================================")
    print("           WELCOME TO THE ATM")
    print("========================================")

    input("\nPress ENTER to insert your ATM card...")

    print("\nReading card... Please wait.")
    time.sleep(2)

    print("\n----------------------------------------")
    print(f"Welcome, {account_holder}!")
    print(f"Account Number: {account_number}")
    print("----------------------------------------")

    while True:

        print("\nPlease choose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Log Out")

        choice = input("\nEnter choice (1-4): ").strip()

        # Check Balance
        if choice == "1":

            print(
                f"\n[BALANCE] Your current balance is: "
                f"${balance:,.2f}"
            )

        # Deposit
        elif choice == "2":

            try:
                amount = float(
                    input("\nEnter amount to deposit: $")
                )

                if amount > 0:

                    balance += amount

                    print(
                        f"[SUCCESS] ${amount:,.2f} "
                        f"deposited successfully."
                    )

                    print(
                        f"New Balance: ${balance:,.2f}"
                    )

                else:
                    print(
                        "[ERROR] Deposit amount must be "
                        "greater than zero."
                    )

            except ValueError:

                print(
                    "[ERROR] Invalid input. "
                    "Please enter a valid number."
                )

        # Withdraw
        elif choice == "3":

            try:
                amount = float(
                    input("\nEnter amount to withdraw: $")
                )

                if amount > balance:

                    print(
                        f"[ERROR] Insufficient funds! "
                        f"Your balance is ${balance:,.2f}"
                    )

                elif amount <= 0:

                    print(
                        "[ERROR] Withdrawal amount must be "
                        "greater than zero."
                    )

                else:

                    balance -= amount

                    print(
                        f"[SUCCESS] ${amount:,.2f} "
                        f"withdrawn successfully."
                    )

                    print(
                        f"Remaining Balance: "
                        f"${balance:,.2f}"
                    )

            except ValueError:

                print(
                    "[ERROR] Invalid input. "
                    "Please enter a valid number."
                )

        # Log out
        elif choice == "4":

            print(
                f"\nThank you for using our ATM, "
                f"{account_holder}. Goodbye!"
            )

            break

        else:

            print(
                "[ERROR] Invalid selection. "
                "Please choose a number from 1 to 4."
            )


if __name__ == "__main__":
    run_atm()
    
