def fib(a,b,n,t):
   if n>0:
      c=a+b
      t.append(c)
      a=b
      b=c
      fib(a,b,n-1,t)
   else:
      return
def power(a,n):
   if n==0:
      return 1
   else:
      return a*power(a,n-1)
t=[]
print("fibanacci series")
fib(-1,1,int(input("enter the limit")),t)
print(t)
print("power of numbers")
print(power((int(input("enter base:"))),int(input("enter power value:"))))
