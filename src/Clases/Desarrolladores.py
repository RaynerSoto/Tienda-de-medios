from General import *
from Medios import *
class Desarrolladores(General):
    persona = 1

    def __init__(self,nombre,personal = 1):
        super(Desarrolladores,self).__init__(nombre)
        self.persona = personal