from Productos import *
from Clientes import *

class Compra:
    def __init__(self, cliente_nit):
        self.cliente_nit = cliente_nit
        self.productos_comprados = []

    def agregar_producto(self, producto):
        self.productos_comprados.append(producto)

    def generar_factura(self):
        total_costo = sum(producto.obtener_precio() for producto in self.productos_comprados)
        impuesto = total_costo * 0.12

        print("Factura:")
        print("Cliente NIT:", self.cliente_nit)
        print("Productos comprados:")
        for producto in self.productos_comprados:
            print(f"- {producto.obtener_nombre()}: {producto.obtener_precio()}")

        print("Total Costo:", total_costo)
        print("Impuesto:", impuesto)
        print("Total a pagar:", total_costo + impuesto)

compras_realizadas = []



def reporte_compra(compra, lista_clientes, lista_productos, impuesto=0.15):
    print(f"------------- REPORTE DE COMPRA {len(compras_realizadas)} -------------")
    
    # Obtener información del cliente
    cliente_nit = compra.cliente_nit
    cliente = next((cliente for cliente in lista_clientes if cliente.obtener_nit() == cliente_nit), None)

    if cliente:
        print("CLIENTE:")
        print(f"Nombre: {cliente.obtener_nombre()}")
        print(f"Correo electrónico: {cliente.obtener_correo()}")
        print(f"Nit: {cliente.obtener_nit()}")
        
        # Listar los productos comprados
        print("ARTÍCULOS COMPRADOS:")
        for i, producto in enumerate(compra.productos_comprados, start=1):
            print(f"{i}. {producto.obtener_nombre()}: Q {producto.obtener_precio():.2f}")

        # Calcular y mostrar el total y los impuestos
        total_costo = sum(producto.obtener_precio() for producto in compra.productos_comprados)
        impuestos = total_costo * impuesto
        
        print(f"Total: Q {total_costo:.2f}")
        print(f"Impuestos: Q {impuestos:.2f}")
        print("------------------------------------------")
    else:
        print("Cliente no encontrado.")
