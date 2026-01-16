"""
Una lista es una secuencia de elementos
Se crea con []
"""

lista1=["Dario", 33, 9.5, True, "German", 20.8]
print(lista1) #Imprime la lista
print(lista1[:]) #Imprime la lista en una rango o posición
print(lista1[2]) #Imprime la posición 2 (9.5)
print(lista1[-1]) #Imprime el último
print(lista1[0:3]) #Imprime de la posición 0 a la 3
print(lista1[3:]) #Imprime del 3 en adelante (no contamos el 3)

lista1.append("Vargas") #Se inserta al final
print(lista1)

lista1.insert(2,"Nadia") #Se inserta con la posición
print(lista1)

lista1.extend(["uno", 1.1, False]) #Agregamos más de un elemento
print(lista1)

lista1.remove(33) #Elimina la primera aparición del valor de la lista (33)
print(lista1)

lista1.pop() #Elimina el último elemento de la lista
print(lista1)

lista2 = ["tres", "cuatro"]
lista3 = lista1 + lista2
print(lista3)

print(lista2*4) #Imprime la lista 4 veces
lista4=[2,1,5,4,3]
print(lista4)
lista4.sort() #Ordena los elementos
print(lista4)

del lista4[0] #Eliminamos el elemento en la posición [0]
print(lista4)

'''
pedir al usuario que ingrese 20 numeros repetidos sin repetir
los almacene en una lista y luego muestra la lista ordenada de menor a mayor,
también nos diga cuantos son repetidos y cuantas veces se repitieron
separarlos entre pareales e impares.
'''