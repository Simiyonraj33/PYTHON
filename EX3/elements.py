l=eval(input("Enter a list: "))
s=set(l)
print(s)
[24bcs176@mepcolinux exp3B]$cat occurence2.py
cat: occurence2.py: No such file or directory
[24bcs176@mepcolinux exp3B]$cat occurrence2.py
s=input("Enter input: ")
d = {}
for ch in s:
   d[ch]=d.get(ch,0)+1
for i,j in sorted(d.items()):
   print(i, "==>", j, "times")
print(d)
