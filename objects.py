class Celestial:
    """Основной класс для планет и их характеристик"""

    def __init__(self, mass=0, x=0, y=0, v=0):
        self.Mass = mass
        self.V = v


    def update_coords(self, x=0, y=0):
        self.X = x
        self.Y = y
        