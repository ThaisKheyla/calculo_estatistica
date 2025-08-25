import time
import psutil
from datetime import datetime

arquivo_csv = "monitoramento.csv"
arquivo_processos = "processos.csv"
cabecalho_monitoramento = "user,dataHora,cpu,ram,disco,temperatura\n"
cabecalho_processos = "pid,nome,cpu,ram\n"

with open(arquivo_csv, "a") as f:
    if f.tell() == 0:
        f.write(cabecalho_monitoramento)

with open(arquivo_processos, "a") as f:
    if f.tell() == 0:
        f.write(cabecalho_processos)

while True:
    user = psutil.users()[0].name
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    uso_cpu = psutil.cpu_percent()
    uso_ram = psutil.virtual_memory().percent
    uso_disco = psutil.disk_usage('/').percent

    try:
        temperatura = psutil.sensors_temperatures().get('coretemp', [])[0].current if psutil.sensors_temperatures() else None
    except Exception as e:
        temperatura = None
        print(f"Erro ao obter temperatura: {e}")

    with open(arquivo_csv, "a") as f:
        f.write(f"{user},{agora},{uso_cpu},{uso_ram},{uso_disco},{temperatura if temperatura else 'N/A'}\n")

    processos = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processos.append([proc.info['pid'], proc.info['name'], proc.info['cpu_percent'], proc.info['memory_percent']])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    with open(arquivo_processos, "a") as f:
        for proc in processos:
            f.write(f"{proc[0]},{proc[1]},{proc[2]},{proc[3]}\n")

    print(f"{user} {agora} cpu: {uso_cpu}% ram: {uso_ram}% disco: {uso_disco}% temperatura: {temperatura if temperatura else 'N/A'}")

    time.sleep(10)
