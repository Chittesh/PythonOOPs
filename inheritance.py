class Parent:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return repr((self.name))


class Child (Parent):
    def __init__(self, name, college):
        super().__init__(name)        #Calling the parent constructor , no need of using self
        self.college = college
    def __repr__(self):
        return repr((super().__repr__(),self.college))

object_parent = Parent('Parent')
object_child = Child('Child','College')

print(object_parent)            #'Parent'
print(object_child)             #("'Child'", 'College')
