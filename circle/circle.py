import math

class Circle():
    pass
class Circle():
    ### INICIALIZAMOS CON RADIUS
    def __init__(self,radius) :
        if radius >= 0 :
            self.radius = radius
        else:
            raise ValueError('El radio debe ser mayor a 0')
                               
    def get_radius(self):
        return self.radius

    def set_radius(self,radius):
        if radius >= 0 :
            self.radius = radius
        else:
            raise ValueError('El radio debe ser mayor a 0')
                
        return self.radius 
    