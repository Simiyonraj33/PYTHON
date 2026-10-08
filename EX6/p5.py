import gc
class student:
   def __init__(self,name):
      self.name=name
      print("Student:",self.name,"created")
   def __del__(self):
      print("Student",self.name,"destroyed")
gc.enable()
s=student("Allan")
print("Calling garbage collector manually")
gc.collect()
print("End of programs")

