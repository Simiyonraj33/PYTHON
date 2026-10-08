# main.py

import factors as f

n = int(input("Enter a positive integer: "))

all_f = f.factors(n)
print(f"Factors of {n}: {all_f}")

prime_f = f.prime_factors(n)
print(f"Prime factors of {n}: {prime_f}")

