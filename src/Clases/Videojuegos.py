from Medios import *
class Videojuegos(Medios):
    desarrollador = ""
    distribuido = ""
    offline = True

    def __init__(self,nombre = "",codigo = "",stock = "",genero = "",precio_venta = "",desarrollador = "",distribuidor = "",offline = False):
        super(Videojuegos).__init__(nombre,codigo,stock,genero,precio_venta)
        self.desarrollador = desarrollador
        self.distribuido = distribuidor
        self.offline = offline

    def __init__(self):
        pass