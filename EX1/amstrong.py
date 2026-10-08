num=int(input("Enter the number: "))
pow=len(str(num))
temp=num
sum=0
while(temp>0):
   digit=temp%10
   sum=sum+(digit**pow)
   temp=temp//10
if(sum==num):
   print("It is an Armstrong number")
else:
   print("Not an Armstrong number")
