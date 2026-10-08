n1=input("Enter the string:")
n2=input("Enter the string:")
opt=' '
i,j=0,0
while(i<len(n1) or j<len(n2)):
   if(i<len(n1)):
      opt=opt+n1[i]
      i+=1
   if  (j<len(n2)):
      opt=opt+n2[j]
      j+=1
print(opt)      

