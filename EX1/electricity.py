unit=float(input("Enter units used: "))
if(unit>=0 and unit<=100):
   bill=unit*10
elif(unit>=101 and unit<=200):
   bill=(100*10)+((unit-100)*15)
elif(unit>=201 and unit<=300):
   bill=(100*10)+(unit*15)+((unit-200)*20)
elif(unit>=301):
   bill=(100*10)+(100*15)+(100*20)+((unit-300)*30)
else:
   print("Invalid input")
print("Bill is: ",bill)
