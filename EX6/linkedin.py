""" based LinkedIn User Management System """
import gc
import sys
class User:
   def __init__(self,name,job):
      self.name = name
      self.job = job
      self.connections = []

   def add_connections(self, connection_name):
      if connection_name not in self.connections:
         self.connections.append(connection_name)
         print(self.name + " Connected With " + connection_name)
      else:
         print(self.name + " Not Connected With " + connection_name)

   def remove_connections(self, connection_name):
      if connection_name in self.connections:
         self.connections.remove(connection_name)
         print(self.name + " Removed Connections With " + connection_name)
      else:
         print("No Connection Found !")

   def view_connections(self):
      print(self.name + "'s connections:")
      if not self.connections:
         print("No Connections Found !")
      else:
         for names in self.connections:
            print(names)

   def show_ref_count(self):
      print("Reference Count for " + self.name + ": " + str(sys.getrefcount(self)))

   def __del__(self):
      print("Objects Destroyed Successfully")


name = input("Enter Your Name : ")
job = input("Enter Job Title : ")
user = User(name,job)
while True:
   print("=====MENU=====")
   print("1. Add Connection")
   print("2. Remove Connection")
   print("3. View Connection")
   print("4. No.Of Reference Object")
   print("5. Delete Object")
   print("6. Exit")
   choice = int(input("Enter Your Choice : "))
   if choice == 1:
      connection_name = input("Enter Name of the Person to be Connected : ")
      user.add_connections(connection_name)
   elif choice == 2:
      connection_name = input("Enter Name of the Person to be Removed : ")
      user.remove_connections(connection_name)
   elif choice == 3:
      if not user.connections:
         print("No Connections Found !")
      else:
         user.view_connections()
   elif choice == 4:
      user.show_ref_count()
   elif choice == 5:
      print("Deleting User...")
      del user
      gc.collect()
   elif choice == 6:
      print("Application Ended !!")
      break
   else:
      print("Invalid Choice !!")
      

