def print_digits (n):
    
    '''hundreds = n // 100
    tens = (n // 10) % 10
    ones = n % 10
    
    print("Hundreds :", hundreds)
    print("Tens :", tens)
    print("Ones :", ones)'''
    
    d1 = n % 10  #Remove last digit
    n = n // 10  #Remove right most digit
    
    d2 = n % 10
    n = n // 10
    d3 = n % 10
    
    print("Hundreds :", d3)
    print("Tens :", d2)
    print("Ones :", d1)

print_digits(312)
