class Paciente():
    def __init__(self,nombre, edad, periodo, m):

        self.nombre = nombre
        self.edad = edad
        self.periodos = periodo
        self.m = m
        self.siguiente = None

    def getsig(self):
        return self.siguiente

    def setsig(self, siguiente):
        self.siguiente= siguiente

        