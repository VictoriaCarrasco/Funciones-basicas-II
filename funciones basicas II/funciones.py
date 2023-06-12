#Función número 1
def contador (numero):
    lista = []
    for i in range (numero,-1,-1):
        lista.append(i)
    return lista
resultado = contador (5)
print (resultado)

#Función número 2
def imprimir_y_devolver (list):
    print (list[0])
    return list [1]
resultado = imprimir_y_devolver ([1,2])
print (resultado)

#Función número 3
def primero_mas_longitud (lista):
    primero = lista[0]
    largo =len(lista)
    suma= primero + largo 
    return suma
resultado = primero_mas_longitud ([1,2,3,4,5])
print (resultado)

#Función número 4
def lista_original (lista):
    if len(lista) < 2:
        return False

    nueva_lista= []
    for num in lista:
        if num > lista[1]:
            nueva_lista.append(num)

    return nueva_lista 

resultado = lista_original ([5,2,3,2,1,4])
longitud = len(resultado)
print (longitud)
print (resultado)

resultado2 = lista_original ([3])
print (resultado2)

#Función número 5
def length_and_Value (tamaño,valor):
    lista = []
    for i in range (tamaño):
        lista.append (valor)
    return lista 
    
resultado = length_and_Value(4,7)
print (resultado)
resultado2 = length_and_Value(6,2)
print (resultado2)