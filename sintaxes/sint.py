print('\n'*50)

#lista ou vetor: É mutável, É ordenado, É indexado de 0...n
lista = [10, 20, 30]
print(lista[2])

#tupla: NÂO é mutável, É ordenado, É indexado de 0...n
tupla = (10, 20, 30)
print(tupla)

# tupla[1] = 5 -> vai dar erro...


#dicionario: É mutável, É ordenado (a partir de v3.7), É INDEXADO
dicionario = {"num01": 10, "num02": 20, "num03": 30}
dicionarioAluno = {"nome": "bob", "idade": 42, "nota": 7.8}
print(dicionarioAluno["nome"])

#Vetor de vetor, ou vetor com mais de uma dimensão, nesse caso 2
matriz = [[10], [20], [30]]

#Matriz 3x3
matriz01 = [[10], [20], [30],
            [40], [50], [60],
            [70], [80], [90]]


print(type(lista))
print(type(tupla))
print(type(dicionario))
print(type(matriz))

