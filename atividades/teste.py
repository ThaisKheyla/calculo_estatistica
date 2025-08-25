import psutil

for proc in psutil.process_iter():
    try:
        pid = proc.pid
        nome = proc.name()
        caminho = proc.exe()
        
        print(f"PID: {pid}, Nome: {nome}, Caminho: {caminho}")
        
       pass 