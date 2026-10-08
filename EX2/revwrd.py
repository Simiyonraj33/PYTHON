n=input("enter the string:")
l=n.split()
l1=[]
i=len(l)-1
while(i>=0):
   l1.append(l[i])
   i=i-1
opt=' '.join(l1)
print(opt)
