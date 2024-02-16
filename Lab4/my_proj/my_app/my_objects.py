class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # I ran into a lot of issues utilizing the code for this section in class. It did not work no matter what. I have adjusted this section. 
    @property
    def wheels(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, color, sound):
        super().__init__(make, model, year)
        self.color = color
        self._sound = sound
        self._wheels = 2

    def honk(self):
        return self._sound

    @property
    def wheels(self):
        return self._wheels

class Car(Vehicle):
    def __init__(self, make, model, year, color, sound):
        super().__init__(make, model, year)
        self.color = color
        self._sound = sound
        self._wheels = 4

    def honk(self):
        return self._sound

    @property
    def wheels(self):
        return self._wheels