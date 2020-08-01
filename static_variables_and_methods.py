class StaticClass:
    #Varibales decalred inside a class is by default static
    count = 0

    def __init__(self,name):
        self.name = name;
        StaticClass.count += 1

    #deaclaring static method
    @staticmethod
    def static_method():
        return StaticClass.count

object_one = StaticClass("chittesh")
object_two = StaticClass("charles")

print(StaticClass.count)
print(object_one.count)

#But if we decalre like below
object_one.count = 100
print(StaticClass.count)
print(object_one.count)
# this will be 100 becasue a new count variabled is created within the scope of object_one which is not recommended

print(StaticClass.static_method())