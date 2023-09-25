#Multiple Inheritance
class Father():
    def gardening(self):
        print("I enjoy gardening")
    def skills():
        print("programming")

class Mother():
    def cooking(self):
        print("I love cooking")
    def skills():
        print("art")

class Child(Father, Mother):
    def sports(self):
        Father.skills()
        Mother.skills()
        print("I enjoy sports")


c = Child()
c.gardening()
c.cooking()
c.sports()

