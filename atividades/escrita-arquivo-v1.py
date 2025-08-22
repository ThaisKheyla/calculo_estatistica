import csv

data_dicts = [
    {'nome': 'Bob', 'idade': 30},
    {'nome': 'Bob', 'idade': 24}
]

fieldnames = ['nome', 'idade']

with open('dados-usuario-v1.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_dicts)