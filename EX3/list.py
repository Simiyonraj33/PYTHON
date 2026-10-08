my_list=[]
while True:
   print("\nList operations: ")
   print("0.Extend an element")
   print("1.Append an element")
   print("2.Insert an element at a specific index")
   print("3.Remove an element")
   print("4.Pop an element")
   print("5.Sort the list")
   print("6.Reverse the list")
   print("7.Find the list")
   print("8.Display the list")
   print("9.EXIT")
   choice=int(input("Enter your choice: "))
   if choice==0:
      elem=input("Enter element: ")
      my_list.extend(elem)
      print("List is: ",my_list)
   elif choice==1:
      elem=input("Enter your choice: ")
      my_list.append(elem)
   elif choice==2:
      index=int(input("Enter index: "))
      elem=input("Enter element to insert: ")
      my_list.insert(index,elem)
      print("List is: ",my_list)
   elif choice==3:
      elem=input("Enter element to remove: ")
      if elem in my_list:
         my_list.remove(elem)
         print("Element removed")
         print("List is:",my_list)
      else:
         print("Element not found!")
   elif choice==4:
      if my_list:
         print("Popped element: ",my_list.pop())
         print("List is: ",my_list)
      else:
         print("List is empty!")
   elif choice==5:
      my_list.sort()
      print("List sorted")
      print("List is: ",my_list)
   elif choice==6:
      my_list.reverse()
      print("List reversed")
      print("List is: ",my_list)
   elif choice==7:
      elem=input("Enter element to find:")
      if elem in my_list:
         print(f"Element found at index:{my_list.index(elem)}")
      else:
          print("Element not found!")
   elif choice==8:
      print("Current List: ",my_list)
   elif choice==9:
      print("Existing...")
      break
   else:
      print("Invalid choice! Please try again")
