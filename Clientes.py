class Clientes:
    def __init__(self, nombre, correo, nit):
        self._nombre = nombre
        self._correo = correo
        self._nit = nit

    def obtener_nombre(self):
        return self._nombre

    def obtener_correo(self):
        return self._correo

    def obtener_nit(self):
        return self._nit
