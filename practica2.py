'''
practica2.py
Crear un programa que tenga un menu con las siguientes opciones:
1. Suma
2. Resta
3. Multilicacion
4. Division
5. Salir
Cada opcion debe ser una funcion diferente
'''

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):

    return a / b

def salir():
    return print(" ")

def main():
    opcion = 0

    while opcion != 5:
        print("\nMENÚ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion=int(input)
        print("Selecciona una opción")
    
    if opcion == 1:
            a = int(input("Ingresa a: "))
            b = int(input("Ingresa b: "))
            print("Resultado:", sumar(a, b))

    elif opcion == 2:
            a = int(input("Ingresa a: "))
            b = int(input("Ingresa b: "))
            print("Resultado:", restar(a, b))

    elif opcion == 3:
            a = int(input("Ingresa a: "))
            b = int(input("Ingresa b: "))
            print("Resultado:", multiplicar(a, b))

    elif opcion == 4:
            a = int(input("Ingresa a: "))
            b = int(input("Ingresa b: "))
            print("Resultado:", dividir(a, b))

    elif opcion == 5:
            print("Saliendo del programa...")

    else:
            print("Opción no válida")

# Punto de entrada
if __name__ == "__main__":
    main()


   