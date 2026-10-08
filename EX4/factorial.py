def fact(x):
   if x==0:
      return 1
   else:
      return x*fact(x-1)
for i in range(0,int(input("enter the limit:"))):
   print((i), "factorial is ",fact(i))
[24bcs176@mepcolinux exp4A]$cat facty.py
def fact(n):
   res=1
   for i in range (i,num+1):
      res*=1
   return res
m=int(input("ENTER A FACTORIAL LIMIT:"))
f=fact(m)
print("{FACTORIAL OF",m,"is",f)
