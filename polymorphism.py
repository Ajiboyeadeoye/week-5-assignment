class Cat:
    def move(self):
        return "All cats catwalk"

class Dog:
    def move(self):
        return "All dogs run"

class Goat:
    def move(self):
        return "All goats walk slowly"


for animal in [Cat(), Dog(), Goat()]:
    print(animal.move())