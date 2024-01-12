import math


class Circle():
    # INICIALIZAMOS CON RADIUS
    def __init__(self, radius):
        if radius >= 0:
            self.radius = radius
        else:
            raise ValueError('El radio debe ser mayor a 0')

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        if radius >= 0:
            self.radius = radius
        else:
            raise ValueError('El radio debe ser mayor a 0')

        return self.radius

    def __mul__(self, n):
        if n >= 0:
            self.radius = self.radius * n
        else:
            raise ValueError(
                'El numero a multiplicar el radio debe ser mayor a 0')
        return self

    def __str__(self):
        return f'Circle con un radio de {self.radius}'


ab = Circle(100)
print(ab)
print(ab.get_radius())
ab.set_radius(10)
print(ab.radius)
ab.__mul__(5)
print(ab.radius)
