import math
print('\n' * 50)

tupla = (1, 2, 3, 4)

print(tupla[2])

for i in range(len(tupla)):
    print(tupla[i])

for valor in tupla:
    print(valor)


lista_temp = list(tupla)
lista_temp[2] = 9
tupla = tuple(lista_temp)
print(tupla)

lista_temp = list(tupla)
for i in range(len(lista_temp)):
    lista_temp[i] = lista_temp[i] + 1
tupla = tuple(lista_temp)
print(tupla)

lista_temp = list(tupla)
if 4 in lista_temp:
    lista_temp.remove(4)
tupla = tuple(lista_temp)
print(tupla)

nova_lista = []
for x in tupla:
    if x > 2:
        nova_lista.append(x)
tupla = tuple(nova_lista)
print(tupla)
