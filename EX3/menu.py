my_list = []

while True:
   print("1. Find Second Largest Element")
   print("2. Find Product Of Elements of the List")
   print("3. Find the elements of given Frequency")
   print("4. Exit")

   choice = int(input("Enter Your Choice : "))

   if choice in [1,2,3]:
      n = int(input("Enter No. of Elements : "))
      for i in range(n):
         ele = int(input(f"Enter Element {i+1} : "))
         my_list.append(ele)

   if choice == 1:
      lst = []
      for num in my_list:
         if num not in lst:
            lst.append(num)
      if len(lst)<2:
         print("No Second Largest Element Found !!")
      else:
         lst.sort()
         print("Second Largest Element:",lst[-2])
   elif choice == 2:
      product = 1
      for num in my_list:
         product = product*num
      print(product)
   elif choice == 3:
      freq = int(input("Enter Frequency : "))
      result = []
      for num in my_list:
         count = 0
         for x in my_list:
            if x == num:
               count += 1
         if count == freq and num not in result:
            result.append(num)
      print(result)
   elif choice==4:
      print("Exiting....")
      break
   else:
      print("Invalid Choice, Enter between 1 - 4.")
