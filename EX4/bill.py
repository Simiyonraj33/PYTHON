def bill(cus_name,order_no,items,d,dis=0,tax=5):
   print("name:",cus_name,"\norder number:",order_no,"\nTax:",tax,"\ndiscount %:",dis)
   s=0
   if d:
      print(d)
      for i in d:
         s+=float(d[i])
   if items:
      print(items)
      for i in items:
         s+=float(items[i])
   s+=((s*(tax/100))-(s*dis/100))
   print("total bill:",s)
   if d:
      print(d)
   print("bill is generated")
itemprice=eval(input("enter the item name and price in dictionary:"))
addchar=eval(input("enter additional charge in dictionary:"))
bill(input("enter name:"),int(input("enter order number:")),itemprice,addchar,float(input("enter the discount%:")),float(input("enter the tax:")))
