class Smartphone:
    def __init__(self, make, color):
        self.make = make
        self.color = color
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.make} {self.color} is now on")
        else:
            print(f"{self.make} {self.color} is already on")
 

class Landphones:
    def __init__(self, weight):
        self.weight = weight

class Smartphone(Landphones):
    pass

smartphone1 = Smartphone(8)
print(smartphone1.weight)
        