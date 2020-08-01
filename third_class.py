class class_name:
    def __init__(self, name='Default'):
        self.name=name
        print("constructor")

    def method(self):
        print("method")

#by default python will pass self as a parameter
object_one = class_name()
object_one.method()
object_two = class_name('Chittesh')
print(object_one.name)
print(object_two.name)
