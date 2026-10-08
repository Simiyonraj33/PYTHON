class MyClass:
    c=0
    def __init__(self, value):
        self.value = value
        MyClass.c += 1
    @classmethod
    def get_object_count(cls):
        return cls.c
obj1 = MyClass(10)
obj2 = MyClass(20)
obj3 = MyClass(30)
print(f"Total number of MyClass objects created:",MyClass.c)
