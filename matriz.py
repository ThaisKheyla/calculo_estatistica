import math
print('\n' * 50)

matriz = [[1, 2], [3, 4]]

print(matriz[1][0])

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])

for linha in matriz:
    for valor in linha:
        print(valor)

matriz[0][1] = 5
print(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = matriz[i][j] + 1
print(matriz)

if 5 in matriz[1]:
    matriz[1].remove(5)
print(matriz)

nova_matriz = []
for linha in matriz:
    if sum(linha) > 5:
        nova_matriz.append(linha)
matriz = nova_matriz
print(matriz)
