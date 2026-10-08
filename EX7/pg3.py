class shape:
    def area(self,x=None,y=None,z=None):
        if x is not None and y is not None and z is not None:
            print("Cuboid Area: ",2*(x*y+y*z+z*x))
        elif x is not None and y is not None:
            print("Rectangle Area: ",x*y)
        elif x is not None:
            print("Square Area: ",x*x)
        else:
            print("No dimensions provided")

#Create Object

s=shape()
s.area(5)
s.area(5,2)
s.area(5,3,4)
