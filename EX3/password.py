p=input("enter password:")
if len(p)<8:
   print("invalid password")
else:
   u=l=d=s=False
   sc="!@#$%^&*(),.?|<>"
   for ch in p:
      if ch.isupper():
         u=True
      if ch.isupper():
         l=True
      if ch.isdigit():
         d=True
      if ch in sc:
         s=True
if s and u and l and d:
   print("valid password")
else:
   print("not valid")
