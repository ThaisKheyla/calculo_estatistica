import math

print('\n' * 50)

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

# 2. a^0 = 1
prop2 = a ** 0

# 3. a^1 = a
prop3 = a ** 1

# 4. a^(-b) = 1/(a^b), a ≠ 0
if a != 0:
    prop4 = a ** (-b)
else:
    prop4 = "Indefinido (a não pode ser zero)"

# 5. a^b * a^c = a^(b+c)
prop5 = (a ** b) * (a ** c)
prop5_check = a ** (b + c)

# 6. (a^b)/(a^c) = a^(b-c), a ≠ 0
if a != 0:
    prop6 = (a ** b) / (a ** c)
    prop6_check = a ** (b - c)
else:
    prop6 = "Indefinido (a não pode ser zero)"
    prop6_check = "Indefinido (a não pode ser zero)"

# 7. (a^b)^c = a^(b*c)
prop7 = (a ** b) ** c
prop7_check = a ** (b * c)

# 8. (a/b)^c = (a^c)/(b^c), b ≠ 0
if b != 0:
    prop8 = (a / b) ** c
    prop8_check = (a ** c) / (b ** c)
else:
    prop8 = "Indefinido (b não pode ser zero)"
    prop8_check = "Indefinido (b não pode ser zero)"

print(f"a^0 = {prop2}")
print(f"a^1 = {prop3}")
print(f"a^(-b) = {prop4}")
print(f"a^b * a^c = {prop5} | a^(b+c) = {prop5_check}")
print(f"(a^b)/(a^c) = {prop6} | a^(b-c) = {prop6_check}")
print(f"(a^b)^c = {prop7} | a^(b*c) = {prop7_check}")
print(f"(a/b)^c = {prop8} | (a^c)/(b^c) = {prop8_check}")