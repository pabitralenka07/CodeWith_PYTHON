while True:
    n = input("Enter a number: ")
    if n == "Quit":
        break
    
    if float(n) < 0:
        print("Negative number ")
    elif float(n) > 0:
        print("Positive number")
    else:
        print("Zero")
        