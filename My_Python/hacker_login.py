import time
import os

USERNAME = "admin"
PASSWORD = "python123"

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")

print("=" * 45)
print("          CYBER LOGIN SYSTEM")
print("=" * 45)

username = input(" Username: ")
password = input(" Password: ")

# Verify credentials
print("\nVerifying credentials", end="")

for i in range(5):
    print(".", end="", flush=True)
    time.sleep(0.5)

if username == USERNAME and password == PASSWORD:

    print("\n\n✓ ACCESS GRANTED")
    print("Welcome,", username)

    print("\nLoading System", end="")

    for i in range(10):
        print(".", end="", flush=True)
        time.sleep(0.2)

    print("\n\n✓ System Ready!")

else:

    print("\n\n✗ ACCESS DENIED")
    print("Invalid Username or Password.")
    
    