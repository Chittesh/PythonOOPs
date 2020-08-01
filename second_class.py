class class_name:
    #this instance varibale has the scope of class
    class_variable = "value"

    #constructor
    #All constructors in python is __init__
    #self is like this varibale in java
    def __init__(self, name, copies):
        self.name = name
        self.copies = copies

    # represenation of the object
    def __repr__(self):
        return repr((self.name,self.copies))


object_one = class_name("Hello Constructor","2");
print(object_one)                   #Hello Constructor
print(object_one.class_variable)    #value
print(object_one.name)              #Hello Constructor