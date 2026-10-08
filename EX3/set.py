while True:
   print("\nSet Operations Menu:")
   print("1. Union")
   print("2. Intersection")
   print("3. Difference")
   print("4. Symmetric Difference")
   print("5. Exit")
   choice = input("Enter your choice (1-5): ")
   if choice == '5':
      print("Exiting the program.")
      break
   ele1 = input("Enter elements of Set A separated by space: ")
   ele2 = input("Enter elements of Set B separated by space: ")
   list1 = ele1.split()  # List for Set A
   list2 = ele2.split()  # List for Set B
   set_a = set(list1)
   set_b = set(list2)
   if choice == '1':
      print("Union:", set_a | set_b)  # set_a.union(set_b)
   elif choice == '2':
      print("Intersection:", set_a & set_b)
   elif choice == '3':
      print("Difference (A - B):", set_a - set_b)
   elif choice == '4':
      print("Symmetric Difference:", set_a ^ set_b)
   else:
      print("Invalid choice! Please enter a number between 1 and 5.")
