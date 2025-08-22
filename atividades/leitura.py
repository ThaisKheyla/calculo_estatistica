import csv
from datetime import datetime, timedelta

arquivo_csv = "monitoramento.csv"

dados = []
with open(arquivo_csv, "r") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        dados.append({
            
            "timestamp": datetime.strptime(linha["timestamp"], "%Y-%m-%d %H:%M:%S"),
            "cpu": float(linha["cpu"]),
            "ram": float(linha["ram"]),
            "disco": float(linha["disco"])
        })
    
while True:
    print("\n1 - média de RAM última hora")
    print("2 - pico de CPU última hora")
    print("3 - média de disco últimos N minutos")
    print("0 - sair")
    escolha = input("escolha uma opção: ")

    agora = datetime.now()

    if escolha == "1":
        soma = cont = 0
        for d in dados:
            if d["timestamp"] >= agora - timedelta(hours=1):
                soma += d["ram"]
                cont += 1
        if cont:
            print(f"uso médio de RAM: {soma/cont:.2f}%")
        else:
            print("não há dados suficientes na última hora.")

    elif escolha == "2":
        pico = 0
        for d in dados:
            if d["timestamp"] >= agora - timedelta(hours=1) and d["cpu"] > pico:
                pico = d["cpu"]
        if pico:
            print(f"pico de CPU: {pico:.2f}%")
        else:
            print("não há dados suficientes na última hora.")

    elif escolha == "3":
        n = int(input("quantos minutos atrás? "))
        soma = cont = 0
        for d in dados:
            if d["timestamp"] >= agora - timedelta(minutes=n):
                soma += d["disco"]
                cont += 1
        if cont:
            print(f"uso médio de disco: {soma/cont:.2f}%")
        else:
            print("não há dados suficientes nesse período.")

    elif escolha == "0":
        break

    else:
        print("opção inválida")
