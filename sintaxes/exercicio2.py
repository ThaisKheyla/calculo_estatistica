import math
print('\n' * 50)

c = float(input("Insira o valor de C: "))
d = float(input("Insira o valor de D: "))

c_elevado_ao_quadrado = math.pow(c, 2)
c_elevado_ao_cubo = math.pow(c, 3)
c_elevado_a_quarta = math.pow(c, 4)
c_elevado_a_d = math.pow(c, d)

print(
    f"\n c elevado ao quadrado: ", c_elevado_ao_quadrado,
    f"\n c elevado ao cubo: ", c_elevado_ao_cubo,
    f"\n c elevado a quarta: ", c_elevado_a_quarta,
    f"\n c elevado a d: ", c_elevado_a_d
)