d = {}

while True:
   print("\nDictionary Operations:")
   print("1. Add a key-value pair")
   print("2. Delete a key")
   print("3. Search for a key")
   print("4. Display dictionary")
   print("5. Clear Dictionary")
   print("6. Pop an Random Element")
   print("7. Display Keys")
   print("8. Display Values")
   print("9. Length of Dictionary")
   print("10. Exit")

   choice = input("Enter your choice: ")

   if choice == '1':
      key = input("Enter key: ")
      value = input("Enter value: ")
      d[key] = value
      print("Key-value pair added.")

   elif choice == '2':
      key = input("Enter key to delete: ")
      if key in d:
         del d[key]
         print("Key deleted.")
      else:
         print("Key not found.")
                                                                                                   
   elif choice == '3':
      key = input("Enter key to search: ")
      if key in d:
         print(f"Key found: {key} -> {d[key]}")
      else:
         print("Key not found.")
   elif choice == '4':
      if d:
         print("\nCurrent Dictionary:")
         for key, value in d.items():
            print(f"{key}: {value}")
      else:
         print("Dictionary is empty.")
   elif choice=='5':
       d.clear()
       print("Dictionary Cleared")
       print(d)
   elif choice == '6':
       d.popitem()
       print("Random Item Deleted ")
   elif choice == '7':
       print(d.keys())
   elif choice == '8':
       for i in d.values():
          print(i)
   elif choice == '9':
      print("Total Length :", len(d))
   elif choice == '10':
      print("Exiting program.")
      break
   else:
      print("Invalid choice. Please try again.")
