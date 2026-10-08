def sum(x,y):
   return x+y
def diff(x,y):
   return x-y
def prod(x,y):
   return x*y
def quot(x,y):
   return x//y
def remind(x,y):
   return x%y
def div(x,y):
   return x/y
while True:
   a=float(input("enter num 1:"))
   b=float(input("enter num 2:"))
   print("menu driven\n1.addition\n2.subtraction\n3.multiplication\n4.quotient\n5.remainder\n6.division\n7.exit")
   ch=int(input("enter the choice:"))
   if ch==7:
      break
   elif ch==1:
      print("sum is:",sum(a,b))
   elif ch==2:
      print("difference is:",diff(a,b))
   elif ch==3:
      print("product is:",prod(a,b))
   elif ch==4:
      print("quotient is:",quot(a,b))
   elif ch==5:
      print("remainder is:",remind(a,b))
   elif ch==6:
      print("values while dividing:",div(a,b))
   else:
      print("invalid choice:try again!")
