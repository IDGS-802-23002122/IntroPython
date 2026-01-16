
from io import open #para indicar la forma de apertura del archivo
import math

lectura=""
texto=open("archivo.txt","r")
lectura= texto.readlines()
print(type(lectura))
print(lectura)
for i in lectura:
    print(i)
texto.close()