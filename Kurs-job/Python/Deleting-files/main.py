import os
import time
import pickle

print("Привет! \nЭто программа обеспечивает полное удаление вашего файл с компьютера!")
time.sleep(1.5)
name = input("Введите имя файла для удаления: ")
size = os.path.getsize(name)
f = open(name, 'wb')
for i in range(size):
    pickle.bump(1, name)
f.seek(0)
for i in range(size):
    pickle.bump(0, name)
f.close()
os.remove(name)