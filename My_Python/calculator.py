print("===== SIMPLE CALCULATOR =====")

# Get numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

if choice == "1":
    result = num1 + num2

elif choice == "2":
    result = num1 - num2

elif choice == "3":
    result = num1 * num2

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

else:
    result = "Invalid choice!"

print("\nResult:", result)

