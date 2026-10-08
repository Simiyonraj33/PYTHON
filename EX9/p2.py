class First:
    def fun(self):
        print('First')
class Second:
    def fun(self):
        print('Second')
class Third:
    def fun(self):
        print('Thrid')
class Four(First, Second):
    def fun(self):
        print('Four')
class Five(Second, Third):
    def fun(self):
        print('Five')
class Six(Four, Five, Third):
    def fun(self):
        print('Six')
s = Six()
s.fun()
print("Answer in MRO:")
print("Method one:")
print(Six.__mro__)
print("Method two:")
print(Six.mro())
                      
