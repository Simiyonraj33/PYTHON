tpl=None
l = []

while True:
   print("1. Create a tuple")
   print("2. Concatenate Tuples")
   print("3. Find Length of the tuples")
   print("4. Count Occurance of an Element")
   print("5. Find Index of a specified Element")
   print("6. Exit")
   choice = int(input("Enter Choice : "))
   if choice == 1:
      n = int(input("Enter No. Of Elements : "))
      for i in range(n):
         ele = int(input(f"Enter Element {i+1} : "))
         l.append(ele)
         tpl = tuple(l)
         print(tpl)
   elif choice == 2:
      tpl2 = tuple(input("Enter Elements : "))
      result = tpl + tpl2
      print("Resultant Tuple:",result)
   elif choice == 3:
      print("Tuple Length :", len(tpl))
   elif choice == 4:
      ele = int(input("Enter Element to Count : "))
      print("Occurances of", ele, ":", tpl.count(ele))
   elif choice==5:
      ele=int(input("Enter Search Element:"))
      if ele in tpl:
         print("Index Of",ele,":",tpl.index(ele))
   elif choice==6:
      print("Existing...")
      break
   else:
      print("Invalid Choice")
