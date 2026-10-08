class student:
   def __init__(self):
      self.n=""
      self.id=7
      self.m1=0
      self.m2=0
      self.m3=0
      self.tot=0
      self.avg=0.0
   def input(self):
     self.n=input("enter the name:")
     self.id=int(input("enter the id:"))
     self.m1=int(input("enter m1:"))
     self.m2=int(input("enter m2:"))
     self.m3=int(input("enter m3:"))
   def find_average(self):
     self.tot=self.m1+self.m2+self.m3
     self.avg=self.tot/3
   def display(self):
     print("the name:",self.n)
     print("ID:",self.id)
     self.find_average()
     print("tot:",self.tot)
     print("average is :",self.avg)
n=int(input("enter the no/: of students:"))
l=[student() for i in range(n)]
for i in l:
   i=student()
   i.input()
   i.display()
