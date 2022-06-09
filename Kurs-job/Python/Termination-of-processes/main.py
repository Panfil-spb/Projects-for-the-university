import psutil

pids = psutil.pids()
for pid in pids:
    try:
        print(pid, psutil.Process(pid).name())
    except:
        pass
pid = int(input("Введите pid процесса который хотите удалить >>> "))
if pid in pids:
    psutil.Process(pid).kill()

for pid in pids:
    try:
        print(pid, psutil.Process(pid).name())
    except:
        pass