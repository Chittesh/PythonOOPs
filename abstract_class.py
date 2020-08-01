from abc import ABC, abstractmethod
class AbstractClass(ABC):
    def abstract_method(self):
        self.method_one()
        self.method_two()
        self.method_three()
    @abstractmethod
    def method_one(self):
        pass

    @abstractmethod
    def method_two(self):
        pass

    @abstractmethod
    def method_three(self):
        pass

class ImplemenataionClass(AbstractClass):
    def method_one(self):
        print("method_one")

    def method_two(self):
        print("method_two")

    def method_three(self):
        print("method_three")


#object_ac = AbstractClass();
object_ac = ImplemenataionClass();
object_ac.abstract_method()



