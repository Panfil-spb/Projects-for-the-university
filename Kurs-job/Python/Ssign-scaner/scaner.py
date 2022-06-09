import os
import time
import psutil
name_of_derr = input("Введите имя дерриктории для сканирования >>> ")
tree = os.walk(name_of_derr)
signature = 'notepad.pdb'
for addrees, dirs, files in tree:
    for file in files:
        name = addrees + '\\' + file
        print(name, end = '\t')

        if name[-1] != '.' and name != '..':
            try:
                f = open(name, 'rb')
                f.seek(121220)
                str = f.read(11)
                if str.decode() == signature:

                    print("DANGER")
                    time.sleep(2)

                else:
                    print(str, end = '\t')
                    print("CLEAR")
            except PermissionError:
                print()
