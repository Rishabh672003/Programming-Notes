# way to make a class with empty body
class person:
    pass


class person2:
    def __init__(self, name, age, SSN, alive):
        self.name = name
        self.age = age
        # _ is just a Convention to point that this attribute is private
        # but it just a convention and still can be accessed and modified
        self._SSN = SSN

        # __ is used to make an attribute protected and its also a convention
        self.__alive = alive

    # _ and __ have the same meaning for methods also
    def sayHello(self):
        print(f"Hello {self.name}!")


class police(person2):
    def __init__(self, name, age, SSN, badge, alive):
        super().__init__(name, age, SSN, alive)
        self.badge = badge

    def sayHello(self):
        print(f"{self.name} is a {self.badge}")


if __name__ == "__main__":
    rahul = person2("rishabh", 20, 69420, alive="yes")
    rahul.sayHello()

    aditya = police("Aditya", 20, 42, "inspector", alive="no")
    aditya.sayHello()
