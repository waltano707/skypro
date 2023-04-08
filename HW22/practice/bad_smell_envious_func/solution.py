class Figure:
    def volume(self):
        ...


class Cube(Figure):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def volume(self):
        return self.x * self.y * self.z


class FigureVolumeCalculator:

    @staticmethod
    def calc_volume(figure: Figure):
        return figure.volume()




