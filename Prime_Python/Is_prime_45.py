def is_prime(n):
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return n > 1

print(is_prime(7))
