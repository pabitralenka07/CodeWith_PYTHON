cart = []

def add_product():
    product = input("Enter product name: ")
    price = float(input("Enter product price: "))

    cart.append([product, price])
    print("Product added successfully!\n")


def view_cart():
    if len(cart) == 0:
        print("Your cart is empty.\n")
    else:
        print("\n---- Shopping Cart ----")
        total = 0

        for item in cart:
            print("Product:", item[0], "| Price:", item[1])
            total += item[1]

        print("Total Bill:", total)
        print()


def remove_product():
    product = input("Enter product name to remove: ")

    for item in cart:
        if item[0].lower() == product.lower():
            cart.remove(item)
            print("Product removed successfully!\n")
            return

    print("Product not found!\n")


while True:
    print("===== Shopping Cart =====")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Remove Product")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_cart()

    elif choice == "3":
        remove_product()

    elif choice == "4":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice!\n")
        