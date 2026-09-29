class xyz:

    def __init__(self,name,age):
        print("Constructor calling")
        self.x = name
        self.y = age

    def __del__(self):
        print("Destructors Executed")

obj1 = xyz("david",27)
print(obj1.x,obj1.y)

del obj1

print("---------------")

obj2 = xyz("yesu",30)
print(obj2.x,obj2.y)

print("----------------")

obj3 = xyz("sam",28)
print(obj3.x,obj3.y)

print("----------------")

obj4 = xyz("mahi",26)
print(obj4.x,obj4.y)

print("----------------")
