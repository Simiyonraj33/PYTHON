p = [x*x for x in range(1,11)]
print("p:",p)
q=[x**3 for x in range(2,6)]
print("q:",q)
r=[x for x in p if x%2==0]
print("r:",r)
print()
s=["Vijay","Swati","Vimal","Parth"]
l=[w[0] for w in s]
print("l:",l)
l1=[10,20,30,40]
l2=[30,40,50,60]
l3=[i for i in l1 if i not in l2]
print("l3:",l3)
l4=[i for i in l1 if i in l2]
print("l4:",l4)
print()
s="Dravid is The Wall".split()
l=[[w.upper(),len(w)]for w in s]
print("l:",l)
print()
