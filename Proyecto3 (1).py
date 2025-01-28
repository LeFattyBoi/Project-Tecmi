print ('---------------------------------------') #AHHHHHHHHHHHHHHHHHHHHHHHHH
print ('⤜    Inventario de almacenamiento    ⤛')
print ('---------------------------------------')

usuario = input ('Favor de proprocionar su nombre: ') #Error aqui ¿"opcion no valida"?

print ('Bienvenido: ',usuario)

inventario = {} #producto y/o cantidades

def agregar (inventario, nombre, cantidad):
    if nombre in inventario:
        inventario [nombre] += cantidad
    else:
        inventario [nombre] = cantidad

def consultar (inventario, nombre):
    return inventario.get (nombre, 'Producto no encontrado') 

while True:
    opcion = input ('Seleccione una opcion \nA) Agregar producto \nB) Consultar producto')
    
    if opcion == 'A': #Agregar producto
        nombre = input ('Ingrese el nombre del producto: ')
        cantidad = int (input ('Ingrese la cantidad del producto: '))
        agregar (inventario, nombre, cantidad)
        print ('Producto agregado correctamente al inventario')
    
    elif opcion == 'B': #Consultar producto
        nombre = input ('Ingrese el nombre del producto: ')
        print ('Consultar: ', consultar (inventario, nombre))
    
    else:
        print ('Opcion no valida')
        break
