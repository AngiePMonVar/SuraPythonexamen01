#3. Construir un programa para ir de compras en un supermercado
# que permita la construcción del siguiente menú:
#1. Digitar 1 para recibir {codigo,nombre,precio} de un producto
#2. Digitar para mostrar todos los productos registrados
#3. Digitar 0 para Salir

i=1

Productos = []

print("***Menú SUPERMERCADO***")

print("1. Agregar productos al carrito de compras: ")

print("2. Mostrar productos del carrito: ")

print("0. SALIR ")



while(i!=0):
    Producto={}
    i=int(input("Digite una opción del Menú: "))
    if(i==1):
        print("Agregar productos al carrito\n")
        Producto['Codigo']=input(f'Ingrese el codigo del producto: ')
        Producto['nombre']=input(f'Ingrese el nombre del producto: ')
        Producto['precio']=input(f'Ingrese el precio del producto: ')
        Productos.append(Producto)
    elif(i==2):
        print("Indique los productos registrados en la canasta\n")
        print(Productos)
    elif(i==0):
        print("Saliendo ..")
        break
    else:
      print("Seleccione la opcion correcta: ")



