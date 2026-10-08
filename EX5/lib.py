class lib:
   bk_count=0
   bk_vac=1000
   d={}
   def __init__ (self):
      self.n=" "
      self.id=0
      self.aut=" "
      self.input()
   def input(self):
      self.n=input("enter book name:")
      self.id=int(input("enter id :"))
      self.aut=input("enter authorname:")
      lib.d[self.id]=self.n
      class book_det:
        def book_count(self):
           lib.bk_count+=1
           lib.bk_vac-=1
           self.display1()
        def display1(self):
           print("available book:",lib.bk__count)
           print("vacancy:",lib.bk_vac)
        def book_find(self,find_id):
           for x in lib.d:
              if find_id==x:
                 self.bkfind_dis(lib.d[x])
        def bkfind_dis(self,n):
           print("book found:")
           print("book found in =",n)
l=lib()
l1=l.input()
l1.bk_count()
m=int(input("enter the id to find:"))
l1.book_find(m)
