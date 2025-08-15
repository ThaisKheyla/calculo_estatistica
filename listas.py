import math
print('\n' * 50)

lista = [10, 20, 30, 40]

print(lista[1])

for i in range(len(lista)):
    print(lista[i])

for valor in lista:
    print(valor)

lista[1] = 25
print(lista)

for i in range(len(lista)):
    lista[i] = lista[i] + 1
print(lista)

if 30 in lista:
    lista.remove(30)
print(lista)

nova_lista = []
for x in lista:
    if x > 20:
        nova_lista.append(x)
lista = nova_lista
print(lista)
