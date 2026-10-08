x=int(input("Enter the number: "))
d = {}
for i in range(x):
   n = input("Enter Name: ")
   m = input("Enter Marks: ")
   d[n] = m
while True:
   n = input("Enter Name for find Marks: ")
   m = d.get(n, -1)
   if m == -1:
      print("Not Found Information")
   else:
      print(n, "==>", m)
   opt = input("Do you want to find another information [Yes|No]? ")
   if opt == "No":
      break
print("Thank you...")
