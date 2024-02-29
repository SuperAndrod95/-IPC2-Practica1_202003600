class Productos:
    def __init__(self, codigo, nombre, descripcion, precio):
        self._codigo = codigo
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
    
    def obtener_codigo(self):
        return self._codigo
    
    def obtener_nombre(self):
        return self._nombre
    
    def obtener_descripcion(self):
        return self._descripcion
    
    def obtener_precio(self):
        return self._precio
