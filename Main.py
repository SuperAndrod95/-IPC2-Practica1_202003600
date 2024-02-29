#Práctica 1 
#Fredy Andrés López Labbé
#Carné: 202003600

from Productos import *
from Clientes import *
from Compras import *


productos = []
clientes = []

opcion = 0
while opcion != 5:
    print("------------------- Menu Principal--------------------")
    print("1. Registrar Producto")
    print("2. Registrar Cliente")
    print("3. Realizar Compra")
    print("4. Reporte de Compra")
    print("5. Datos del Estudiante")
    print("6. Salir")
    print("------------------------------------------------------")
    
    opcion = int(input())

    if opcion == 1:
        codigo = input("Inserte código:")
        nombre = input("Inserte el nombre del producto:")
        descripcion = input("Inserte una descripcion del producto:")
        precio = float(input("Inserte el precio del producto:"))

        nuevo_producto = Productos(codigo, nombre, descripcion, precio)
        productos.append(nuevo_producto)

        print("Producto registrado correctamente")

    elif opcion == 2:
        Name = input("Inserte nombre del cliente")
        correo = input("Inserte correo del cliente")
        nit = input("Inserte nit del cliente")

        nuevo_cliente = Clientes(Name, correo, nit)
        clientes.append(nuevo_cliente)
        print("Cliente registrado correctamente")

    elif opcion == 3:
        nit_cliente = input("Ingrese el NIT del cliente: ")

        cliente_existente = next((cliente for cliente in clientes if cliente.obtener_nit() == nit_cliente), None)

        if cliente_existente:
            compra_actual = Compra(cliente_nit=nit_cliente)

            while True:
                print("---------------- Menú Compra ----------------")
                print("1. Agregar Producto")
                print("2. Terminar Compra y Facturar")
                print("3. Regresar")
                print("---------------------------------------------")
                option = int(input())

                if option == 1:
                    codigo_producto = input("Ingrese el código del producto: ")
                    producto_existente = next((producto for producto in productos if producto.obtener_codigo() == codigo_producto), None)

                    if producto_existente:
                        compra_actual.agregar_producto(producto_existente)
                        print(f"Producto '{producto_existente.obtener_nombre()}' agregado a la compra.")
                    else:
                        print("Producto no encontrado.")
                elif option == 2:
                    compra_actual.generar_factura()
                    compras_realizadas.append(compra_actual)
                    print("Compra finalizada. Factura generada.")
                    break
                elif option == 3:
                    print("Compra cancelada. Regresando al menú principal.")
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
        else:
            print("Cliente no encontrado.")

    elif opcion == 4:
        if compras_realizadas:
            for i, compra in enumerate(compras_realizadas, start=1):
                reporte_compra(compra, clientes, productos)
        else:
            print("No hay compras realizadas.")
        pass
  
    elif opcion == 5:
        print("-------------------------------------------------------")
        print("--- Introducción a la Programación y Computación 2 ----")
        print("--------------------- Sección P -----------------------")
        print("------- Fredy Andrés López Labbé, Carné:202003600 -----")
        print("-------------------------------------------------------")
        break
    elif opcion == 6:
        break