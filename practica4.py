#practica4
'''
pedir al usuario que ingrese 20 numeros repetidos sin repetir
los almacene en unalista y luego muestra la lista ordenada de menor a mayor,
también nos diga cuantos son repetidos y cuantas veces se repitieron
separarlos entre pareales e impares.
'''
import os

def main():
    print("Ingresa 20 números")

    lista=[]
    pares=[]
    impares=[]
    repetidos=[]

    for i in range(20):
        numero=int(input("Numero {}:".format(i+1)))
        lista.append(numero)
        if(list.count(numero)>1):
          repetidos.append(numero)

        if(numero%2==0):
            pares.append(numero)
        else:
            impares.append(numero)
        
    lista.sort()
    print("Lista ordenada:",lista)
    print("Pares:",pares)
    print("Impares:",impares)
    print("Repetidos:",repetidos)
    os.system("pause")
    
    
    


if __name__ == "__main__":
    main()

