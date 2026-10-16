start = int(input("Start: "))
end = int(input("End: "))

for n in range(start, end + 1):
    if n < 2:
        continue
        
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        print(n, end=" ")