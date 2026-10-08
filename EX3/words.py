h=input("enter the string:")
l=h.split()
l1=[]
i=len(l)-1
while i>=0:
   l1.append(l[i])
   i=i-1
p=' '.join(l1)
print(p)
