s=input("Enter the string:")
l=s.split()
if(len(l)==2):
   print("The length of the string is:",len(l))
   s1=l[0]
   s2=l[1]
   s3=s2[0]+s1[1:]
   s4=s1[0]+s2[1:]
   print("After swapping:",s3,s4)
else:
   print("Invalid")
