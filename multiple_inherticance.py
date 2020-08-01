class Parnet_one:
    def method_one(self):
        print("Parent_method_1")

class Parnet_two:
    def method_two(self):
        print("Parent_method_2")

class child(Parnet_one, Parnet_two):
    pass

object_child = child();
object_child.method_one()
object_child.method_two()