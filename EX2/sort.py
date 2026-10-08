n=input("Enter the string:")
n1=n2=opt=' '
for x in n:
   if (x.isalpha()):
      n1=n1+x
   else:
      n2=n2+x
for x in sorted(n1):
   opt=opt+x
for x in sorted(n2):
   opt=opt+x
print(opt)   

