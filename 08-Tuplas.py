'''
Las tuplas son inmutables
se declaran con ( )
'''

tupla=("uno", "dos", "tres")
print(tupla)
5
tuplasVariosDatos=(12, True,23.5,"El gato",12+4)

tuplasVariosTuplas=(1,2,3,4,(1,2,3))
print(tuplasVariosDatos)

print(tuplasVariosDatos[3])
print(tuplasVariosDatos[-2])
print(tuplasVariosDatos[0:2])

a,b,c=tupla
print(a,b,c)