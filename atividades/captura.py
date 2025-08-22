import psutil

cpu = psutil.cpu_times(percpu=False)
cpu_percent = psutil.cpu_percent(interval=1)

print("passei por aqui")
print("Usuário: ", cpu.user)