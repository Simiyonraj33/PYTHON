def factors(n):
   return [i for i in range(1,n+1)if n%i==0]
def is_prime(num):
   if num<=1:
      return False
   return all(num%i!=0 for i in range(2,int(num**0.5)+1))
def prime_factors(n):
   return[i for i in factors(n) if is_prime(i)]
