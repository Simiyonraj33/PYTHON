rows = int(input("Enter No. Of Rows : "))
cols = int(input("Enter No. Of Coloumns : "))
A=[]
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
   r1 = []
   for j in range(cols):
      b = 0
      for k in range(cols):
         b += A[i][k] * B[k][j]
         r1.append(b)
      result.append(r1)
for i in range(rows):
   for j in range(cols):
      print(result[i][j], end = ' ')
   print()
