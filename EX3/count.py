n=input("enter the string:").lower()
p="aeiou"
v=c=0
for ch in n:
   if ch in p:
      v=v+1
   else:
      c=c+1
print(f"vowels:{v}")
print(f"consonants:{c}")
