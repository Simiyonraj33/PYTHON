def consdup(n):
   s=''
   for i in range(len(n)):
      if (i<len(n)-1 and n[i]==n[i+1]):
         continue
      else:
         s+=n[i]
   return s
x=input("enter the string:")
print(consdup(x))
