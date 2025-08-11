import math
print('\n' * 50)

numero = 3.14159

print(f"\n Original: {numero}", 
      f"\n Arredondado para 2 casas: {round(numero, 2)}", 
      f"\n Arredondado para 3 casas: {round(numero, 3)}", 
      f"\n Arredondado para 0 casas: {round(numero, 0)}")

#A função round é uma função embutida 
# (built-in) do Python, ou seja, já faz parte 
# da linguagem e está disponível automaticamente,
#  sem necessidade de importação.