w = input("Enter String:")
s = set(w)
v = {'a', 'e', 'i', 'o', 'u'}
d = s.intersection(v)
print("Vowels",w,":",d)
