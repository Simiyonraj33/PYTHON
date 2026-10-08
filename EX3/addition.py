rows = int(input("Enter No. Of Rows : "))
cols = int(input("Enter No. Of Coloumns : "))
A = []
print("Enter A Matrix")
for i in range(rows):
   row = []
   for j in range(cols):
      value = int(input())
      row.append(value)
   A.append(row)
B = []
print("Enter B Matrix")
for i in range(rows):
   row = []
   for j in range(cols):
      value = int(input())
      row.append(value)
   B.append(row)

result = []
for i in range(rows):
   row = []
   for j in range(cols):
      r = A[i][j]  + B[i][j]
      row.append(r)
   result.append(row)

print("Sum of 2 Matrix")
for i in range(rows):
   for j in range(cols):
      print(result[i][j] , end = ' ')
   print()
