n=int(input("Enter the range: "))
l=[]
for i in range(n):
   ele=input(f"Enter element{i+1}: ")
   l.append(ele)
s=len(l)
l1=[]
while s>0:
   l1.append(l[s-1])
   s=s-1
print("Reversed list: ",end='')
print(l1)
