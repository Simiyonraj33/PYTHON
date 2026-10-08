def handle_exceptions():
   try:
      print("1.zero division error.")
      a=int(input("enter a value to be divided by 0:"))
      print(a/0)
   except ZeroDivisionError as e:
      print("error:",e)
   try:
      print("\n2.Value error")
      num=int(input("enter a string:"))
      print(num)
   except ValueError as e:
      print("error:",e)
   try:
      print("\n3.Index error:")
      my_list=[1,2,3]
      print(my_list)
      print(my_list[int(input("enter an index not list:"))])
   except IndexError as e:
      print("error:",e)
   try:
      print("\n4.key error:")
      my_dict={"name":"alice"}
      print(my_dict)
      print(my_dict[input("enter a key not in the dictionary:")])
   except KeyError as e:
      print("error:",e)
   try:
      print("\n5.type error:")
      n=input("enter a string to add to 10:")
      print(10+n)
   except TypeError as e:
      print("error:",e)
   try:
      print("\n6.floating-point division error:")
      n1=float(input("enter a float number to divide 0.0:"))
      print(n1/0.0)
   except ZeroDivisionError as e:
      print("error:",e)
handle_exceptions()      
