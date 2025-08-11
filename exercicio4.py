import math
print('\n' * 50)

#salário
w = 3345.61

piso_salarial = math.floor(w)
teto_salarial = math.ceil(w)
print(
    f"\n Piso salárial: {piso_salarial}",
    f"\n Teto salárial: {teto_salarial}",
    f"\n Valor arredondado: {round(w, 0)}"
)