import psutil

mem = psutil.virtual_memory()

print(f"Total de memória RAM: {mem.total / (1024**3):.2f} GB")
print(f"Memória disponível: {mem.available / (1024**3):.2f} GB")
print(f"Uso de memória: {mem.used / (1024**3):.2f} GB")
print(f"Percentual de uso: {mem.percent}%")
