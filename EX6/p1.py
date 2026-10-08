class Scientist:
    def __init__(self):
        self.n="Dr.APJ.Abdul Kalam"
        self.i=self.info()
    def method(self):
        print("Name:",self.n)
    class info:
        def __init__(self):
            self.h=5.7
            self.w=70
            self.c="Dark"
        def method(self):
            print("Height:{}\nWeight:{}\nColor:{}".format(self.h,self.w,self.c))
s=Scientist()
s.method()
o=s.info()
o.method()
