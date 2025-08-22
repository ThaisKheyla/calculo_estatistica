import psutil
import time
from datetime import datetime

arquivo_csv = "monitoramento.csv"
cabecalho = "user,timestamp,cpu,ram,disco\n"

with open(arquivo_csv, "a") as f:
    if f.tell() == 0:
        f.write(cabecalho)

while True:
    user = psutil.users()[0].name
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    uso_cpu = psutil.cpu_percent()
    uso_ram = psutil.virtual_memory().percent
    uso_disco = psutil.disk_usage('/').percent

    with open(arquivo_csv, "a") as f:

                # giuliana,2025-08-18 10:00:10,40.1,63.0,50.2
        f.write(f"{user}, {agora},{uso_cpu},{uso_ram},{uso_disco}\n")

    print(f"{user} {agora} cpu: {uso_cpu}% ram: {uso_ram}% disco: {uso_disco}%")

    time.sleep(10)
