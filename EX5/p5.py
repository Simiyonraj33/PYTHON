class NegativeIntegerException(Exception):
   def __init__(self,m="enter the positive integer for id:"):
      self.msg=m
class lib:
   bk_count=0
   bk_vacancy=1000
   d={}
   def __init__(self):
      self.__n=""
      self.__id=3
      self.__aut=""
      self.input()
   def input(self):
      self.__n=input("enter the name:")
      self.__id=int(input("enter the id:"))
      self.__aut=input("enter the author name:")
      lib.d[self.__id]=self.__n
      lib.inc_count()
   @classmethod
   def inc_count(cls):
         cls.bk_count+=1
         cls.bk_vacancy-=1
   @staticmethod
   def display():
         print("1.Total books:",lib.bk_count)
   @classmethod
   def find_book(cls,ids):
         for x in lib.d:
            if ids==x:
               lib.print_book(lib.d[x])
   @staticmethod
   def print_book(n):
         print("2.The name of the book for the gn id is :",n)
   def vacancy(self):
      print("3.The vacancy in the lib is:",lib.bk_vacancy)
try:
   n=int(input("enter the number of books to add:"))
   l=[lib() for i in range(n)]
   for i in l:
      i.display()
      bk_id=int(input("enter the id to find the book:"))
      i.find_book(bk_id)
      i.vacancy()
      break
except NegativeIntegerException as n:
   print(n.msg)
except ValueError:
   print("Enter a integer value for id to find the book:")
print(lib.id)

