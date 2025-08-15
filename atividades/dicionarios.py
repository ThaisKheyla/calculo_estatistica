import math
print('\n' * 50)

d = {"nome": "Ana", "idade": 25}
print(d["nome"])
for k in d:
    print(k, d[k])
d["idade"] = 30
print(d)
del d["nome"]
print(d)
