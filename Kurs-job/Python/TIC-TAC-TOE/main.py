import time


def field_start():#меню для показа расстановки
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8")

def field_game():
    print(f"{Moves[0]} | {Moves[1]} | {Moves[2]}")
    print(f"---------")
    print(f"{Moves[3]} | {Moves[4]} | {Moves[5]}")
    print(f"---------")
    print(f"{Moves[6]} | {Moves[7]} | {Moves[8]}")

def start_menu():
    print("Привет! Это игра 'Крестики Нолики'!")
    #time.sleep(1)
    print("Вот ваше поле для игры.")
    #time.sleep(1)
    print("Чтобы заполнить ячейку своей фигурой надо ввести цифру соответсвующая номеру этой ячейки!")
    #time.sleep(1.5)
    field_start()
    #time.sleep(2)
    print("В этой версии игры вы будете играть с компьютером!")
    #time.sleep(1)
    print("Попытайтесь его обойти в этой непростой игре;)")

def side_choice():
    while True:
        Human = input("Введите X(x), если хотите ходить первым, или O(o)(буква), чтобы ходить вторым >>> ")
        if Human.lower() == 'x' or Human.lower() == 'х':
            Human, Computer = 'X', 'O'
            print("Отлично! Вы начинаете ходить первым!")
            time.sleep(1)
            break
        elif Human.lower() == 'o' or Human.lower() == 'о':
            Human, Computer = 'O', 'X'
            print("Отлично! Вы начинаете ходить вторым!")
            time.sleep(1)
            break
        else:
            print("Введите X или O")
    return Human, Computer

def Victory_Check():
    Victory_Choise = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
    for i in Victory_Choise:
        if Moves[i[1]] == Moves[i[0]] and Moves[i[1]] == Moves[i[2]] and Moves[i[0]] != ' ':
            return Moves[i[0]]
    return ' '



def Human_Move():
    while True:
        while 1:
            try:
                choice = int(input("Введите номер ячейки куда хотите походить >>> "))
            except ValueError:
                print("Введите число от 0 до 9!")
            if choice >= 0 or choice < 10:
                break
        if Moves[choice] != ' ':
            print("Выберете другую ячейку! Эта уже занята!")
        else:
            return choice

def Computer_Move():
    Copy_Moves = [i for i in Moves]
    Best_Move = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    for i in range(9):
        if Copy_Moves[i] == ' ':
            Copy_Moves[i] = Computer
            win = Victory_Check_Computer(Copy_Moves)
            if win == Computer:
                return i
            Copy_Moves[i] = ' '
    for i in range(9):
        if Copy_Moves[i] == ' ':
            Copy_Moves[i] = Human
            win = Victory_Check_Computer(Copy_Moves)
            if win == Human:
                return i
            Copy_Moves[i] = ' '
    for i in Best_Move:
        if Copy_Moves[i] == ' ':
            return i

def Victory_Check_Computer(Copy_Moves):
    Victory_Choise = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
    for i in Victory_Choise:
        if Copy_Moves[i[1]] == Copy_Moves[i[0]] and Copy_Moves[i[1]] == Copy_Moves[i[2]] and Copy_Moves[i[0]] != ' ':
            return Copy_Moves[i[0]]
    return ' '



"""_____________________________________________________________________"""







Human, Computer = '', ''
start_menu()
#time.sleep(1)
Human, Computer = side_choice()
Winner = ''
Number_Of_Moves = 0
Moves = [' ' for i in range(9)]
Move_Game = 'X'
while Winner != 'X' or Winner != 'O' or Number_Of_Moves != 9:
    field_game()
    if Number_Of_Moves == 9:
        break
    if Human == Move_Game:
        move = Human_Move()
        Moves[move] = Human
        Winner = Victory_Check()
        if Winner != ' ':
            break
        Move_Game = Computer
        Number_Of_Moves += 1
        continue
    elif Computer == Move_Game:
        move = Computer_Move()
        Moves[move] = Computer
        Winner = Victory_Check()
        if Winner != ' ':
            break
        Move_Game = Human
        Number_Of_Moves += 1
        continue


if Number_Of_Moves == 9:
    print("Ничья! Попробуй ещё раз!")
elif Winner == Computer:
    print("Победа искусственного интеллекта! В следующий раз повезёт больше!")
elif Winner == Human:
    print("Победа человека! Ты молодец!")