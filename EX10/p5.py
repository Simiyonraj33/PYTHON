from zipfile import *
def zipfile():
   f=ZipFile("f.zip","w",ZIP_DEFLATED)
   f.write("f1.txt")
   f.write("f2.txt")
   f.write("f3.txt")
   f.close()
   print("f.zip created successfully")
def unzipfile():
  f=ZipFile("f.zip",'r',ZIP_STORED)
  n=f.namelist()
  for n1 in n:
    print("File Name:",n1)
    print("File Data:")
    f1=open(n1,'r')
    print(f1.read())
    print()
while True:
   print("1.Zipping Files")
   print("2.Unzipping Files")
   print("3.Exit")
   ch=input("Enter a Choice:")
   if ch=='1':
      zipfile()
   elif ch=='2':
      unzipfile()
   elif ch=='3':
      break
   else:
      print("Invalid Choice")
