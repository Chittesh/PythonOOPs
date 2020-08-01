from abc import ABC, abstractmethod
class AbstractClass(ABC):
    def abstract_method(self):
        self.method_one()
    @abstractmethod
    def method_one(self):
        pass

#Impelemenation 1
class ImplemenataionClass(AbstractClass):
    def method_one(self):
        print("method_one")
#Impelemenation 2
class ImplemenataionClass_2(AbstractClass):
    def method_one(self):
        print("method_one_Two")
#creating a list
object_ac = [ImplemenataionClass(),ImplemenataionClass_2()]
for i in object_ac:
    i.method_one()




