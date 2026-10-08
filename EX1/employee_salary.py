bp=float(input("Enter the basic pay of the employee: "))
grade=input("Enter grade of the employee: ")
if(grade=='A'):
   allow=1700
elif(grade=='B'):
   allow=1500
elif(grade=='C'):
   allow=1000
else:
   print("No grade")
hra=0.5*bp
da=0.2*bp
pf=0.11*bp
np=bp+hra+da+allow-pf
print("Net pay of the employee is: ",np)
