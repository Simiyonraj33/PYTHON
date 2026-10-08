n=input("Enter the string:")
l=[]
for x in n:
   if(x not in l):
      l.append(x)
opt=''.join(l)
print(opt)
