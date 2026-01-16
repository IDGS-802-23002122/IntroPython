'''
Practica1.py
operacon de multiplicación de a x b usando sumas
a=3
b=4
salida: 3+3+3+3=12
'''

# Practica1.py
# Multiplicación usando sumas

a = 3
b = 4

contador = 0
resultado = 0
tem = ""

while contador < b:
    resultado += a
    contador += 1
    tem += str(a)
    if contador < b:
        tem += "+"

tem += "=" + str(resultado)

print(tem)
