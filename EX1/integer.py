n=int(input("Enter a number: "))
for i in range(1,n+1):
   if(i%3==0 and i%5==0):
      print("XYZABC")
   elif(i%3==0):
      print("ABC")
   elif(i%5==0):
      print("XYZ")
   else:
      pass
