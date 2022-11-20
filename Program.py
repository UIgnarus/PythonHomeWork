import os
import random


def clear(): return os.system('cls')


def game_start():
    clear()
    print("=======================\n" +
          "====Крестики-нолики====\n" +
          "=======================\n")


def game_mode():
    print("Введите (1), если хотите играть с другом\n" +
          "Введите (2), если хотите играть с ботом")
    mode = int(input("-->"))
    if not (mode == 1 or mode == 2):
        print("Неверное число!")
        game_mode()
    clear()
    return mode - 1


def player_name(mode):
    print("Введите имя первого игрока (x): ", end="")
    player_1 = input()
    if not mode:
        print("Введите имя второго игрока (o): ", end="")
        player_2 = input()
    else:
        print("\nВторой игрок - Bot \n")
        player_2 = "Bot"
    clear()
    return player_1, player_2


def goes_first(player_1, player_2):
    while True:
        print("Выберите кто ходит первый!\n"
              + f"(1) - игрок {player_1}\n"
              + f"(2) - игрок {player_2}\n"
              + "(3) - Рандом\n")
        turn = int(input("-->"))
        if 1 <= turn <= 3:
            clear()
            return turn
        else:
            print("Не то количество конфет!")


field = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]


win_list = [[[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]]]


def line_to_value(line, f=field):
    value = []
    for i in line:
        value.append(f[i[0]][i[1]])
    return value


def print_pole(f=field):
    print("  1 2 3 - x")
    i = 1
    for item in f:
        print(f"{i} ", end="")
        i += 1
        print(*item)
    print("|\ny")


def find_win(f=field):
    i = 0
    for line in win_list:
        value = line_to_value(line)
        if value[0] == value[1] == value[2] != "-":
            return 1
        if not "-" in value:
            i += 1
            if i == 8:
                return 2
    return 0


def find_in_line(amount_x, amount_o):
    for line in win_list:
        value = line_to_value(line)
        x = 0
        o = 0
        for i in range(3):
            if value[i] == "x":
                x += 1
            if value[i] == "o":
                o += 1
        if x == amount_x and o == amount_o:
            return line


def player_turn(symbol):
    while True:
        text = "Введите координату поля\n"\
            + "в формате x y, через пробел\n"\
            + "например: 2 2\n"\
            + "-->"
        c = [int(i) - 1 for i in input(text).split()]
        if field[c[1]][c[0]] == "-":
            field[c[1]][c[0]] = symbol
            break
        else:
            print("Уже занято!")


def line_recording(line, symbol):
    for i in range(0, 3):
        if line[i] == "-":
            line[i] = symbol
            break


def print_player(x, s): print(f"\nХод игрока {x} - ({s})\n")
def victories(x, s): print(f"\n\nПобедил игрок {x} - ({s})!")


def tic_tac_toe(player_1, player_2):
    game_flag = True
    first = goes_first(player_1, player_2)
    if first == 3:
        first = random.randint(0, 1)
    else:
        first %= 2
    if not player_2 == "Bot":
        clear()
        while game_flag:
            print("\n")
            if first:
                print_pole()
                print_player(player_1, "x")
                player_turn("x")
                status = find_win()
                if status == 1:
                    game_flag = False
                elif status == 2:
                    first = 2
                    break

                clear()
                first = False
            else:
                print_pole()
                print_player(player_2, "o")
                player_turn("o")
                first = True
                status = find_win()
                if status == 1:
                    game_flag = False
                elif status == 2:
                    first = 2
                    break
                clear()
                first = True
        if first == 2:
            clear()
            print_pole()
            print("Ничья!")
        elif first:
            print_pole()
            victories(player_2, "o")
        else:
            print_pole()
            victories(player_1, "x")
    else:
        clear()
        while game_flag:
            print("\n")
            if first:
                print_pole()
                print_player(player_1, "x")
                player_turn("x")
                status = find_win()
                if status == 1:
                    game_flag = False
                elif status == 2:
                    first = 2
                    break

                clear()
                first = False
            else:
                print_pole()
                print_player(player_2, "o")
                player_turn("o")
                first = True
                status = find_win()
                if status == 1:
                    game_flag = False
                elif status == 2:
                    first = 2
                    break
                clear()
                first = True
        if first == 2:
            clear()
            print_pole()
            print("Ничья!")
        elif first:
            print_pole()
            victories(player_2, "o")
        else:
            print_pole()
            victories(player_1, "x")


def main():
    game_start()
    mode = game_mode()
    player_1, player_2 = player_name(mode)
    tic_tac_toe(player_1, player_2)


main()
# print(find_win())
