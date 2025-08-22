import pandas as pd

dados = {
    "nome": ["Bob", "Tom", "Mel"],
    "idade": [10, 42, 19]
}

df = pd.DataFrame(dados)

print(type(dados))
print(type(df))

df.to_csv("dados-usuario-v2.csv", encoding="utf-8", index=False)