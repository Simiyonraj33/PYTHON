class Shape:
   def area(self,*args):
      if(len(args))==1:
         radius=args[0]
         print("Circle Area: ",3.14*radius*radius)
      elif(len(args))==2:
         length,width=args
         print("Rectangle Area: ",length*width)
      elif(len(args))==3:
         length,width,height=args
         print("Cuboid Area: ",2*(length*width+width*height+height*length))
      else:
         print("Invalid number of arguments")

#"Object creating"
s=Shape()
s.area(5,3,4)
s.area(2,7)
s.area(5)
s.area()
