a = 5
b = 9
sum = a+b

# Normal formatting
print("Language is {}".format("python"))
print("Sum of {} & {} is {}".format(a,b,sum))

# Index formatting
print("Sum of {1} & {0} is {2}".format(a,b,sum))

# Value based formatting
print("Values of vars {a} & {b}".format(a=5,b=10))
