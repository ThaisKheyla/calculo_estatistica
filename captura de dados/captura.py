import psutil
import csv

# Captura de processos da cpu e memoria
processos = []
for p in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_info']):
    try:
        processos.append({
            'pid': p.info['pid'],
            'nome': p.info['name'],
            'usuario': p.info['username'],
            'cpu_percent': p.info['cpu_percent'],
            'memoria_rss': p.info['memory_info'].rss
        })
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# Salvar csv de processos
with open('processos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['pid', 'nome', 'usuario', 'cpu_percent', 'memoria_rss'])
    writer.writeheader()
    writer.writerows(processos)
print("CSV de processos gerado!")

# Captura de io e threads
processos_io = []
for p in psutil.process_iter(['pid', 'name', 'num_threads', 'io_counters']):
    try:
        io = p.info['io_counters']
        processos_io.append({
            'pid': p.info['pid'],
            'nome': p.info['name'],
            'threads': p.info['num_threads'],
            'bytes_lidos': io.read_bytes,
            'bytes_escritos': io.write_bytes
        })
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# Salvar arquiv csv 
with open('processos_io.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['pid', 'nome', 'threads', 'bytes_lidos', 'bytes_escritos'])
    writer.writeheader()
    writer.writerows(processos_io)
print("CSV de I/O gerado!")


# O psutil retorna os dados de formas diferentes, às vezes em dicionários,
# às vezes em objetos, então precisei filtrar informações q não são tão necessárias e formatar alguns campos,
# como por exemplo a memória e nomes, pra deixar tudo organizado e padronizado no csv. 