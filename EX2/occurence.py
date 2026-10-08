n=input("Enter the string:")
d={}
for x in n:
   if(x in d.keys()):
      d[x]=d[x]+1
   else:
      d[x]=1
for i,j in d.items():
   print("{}={} times".format(i,j))
