def prime_factors(factors, n):
    factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            factors.append(i)
            n //= i
           
    
    return factors
number = int(input("Enter a number: "))
print("Prime factors of", number, "are:", prime_factors([], number))