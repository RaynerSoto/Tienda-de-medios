from  General import  *
class Medios(General):
    codigo = ""
    stock = 0
    genero = ""
    precio_venta = 0

    def __init__(self,nombre='',codigo="",stock="",genero="",precio_venta=0):
        super(Medios,self).__init__(nombre)
        self.codigo = codigo
        self.stock = stock
        self.genero = genero
        self.precio_venta = precio_venta

    def get_nombre(self):
        return self.nombre