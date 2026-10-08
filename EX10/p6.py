import csv
with open("emp.csv",'w',newline='') as f:
    w=csv.writer(f)
    w.writerow(["ENO","ENAME","ESAL","EADDR"])
    n=int(input("Enter the no of employee:"))
    for i in range(n):
        eno=input("Employee emp no:")
        ename=input("Enter the emp name:")
        esal=input("Enter the emp salary:")
        eaddr=input("Enter the emp address:")
        w.writerow([eno,ename,esal,eaddr])
print("Employees data written into csv file")

