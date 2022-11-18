import os
import math
import random
def clear(): return os.system('cls')


def start():
    clear()
    print("=======================\n" +
          "========28 конфет!=====\n" +
          "=======================\n" +
          "press enter\n")
    launch = input("-->")
    if not launch == "":
        launch = False
    else:
        launch = True


def game_mode():
    print("Введите (1), если хотите играть с другом\n" +
          "Введите (2), если хотите играть с ботом")
    mode = int(input("-->"))
    if not (mode == 1 or mode == 2):
        print("Неверное число!")
        game_mode()
    return mode


def player_name(mode):
    print("Введите имя первого игрока: ", end="")
    player_1 = input()
    if mode == 1:
        print("Введите имя второго игрока: ", end="")
        player_2 = input()
    else:
        print("\nВторой игрок - Bot \n")
        player_2 = "Bot"
    return player_1, player_2


def bot(all_candy):
    if all_candy > 56:
        result = (all_candy%28) + 1
        print(f"Bot выбрал {result}")
        return result
    else:
        if all_candy > 29:
            result = (all_candy%28) - 1
            print(f"Bot выбрал {result}")
            return result
        elif all_candy > 28:
            return 1
        else:
            print(f"Bot выбрал {all_candy}")
            return all_candy


def test_bot():

    n = 2021
    print(f"\n\nCandy' = {n}")
    i = 0
    while n > 0:
        print(f"Bot '{i+1}' = {bot(n)}")
        n -= bot(n)
        print(f"Candy' = {n}")
        i += 1
        i %= 2


def player_turn(player):
    print(f"Ход игрока {player}: ", end="")
    turn = int(input())
    if 1 <= turn <= 28:
        return turn
    else:
        print("Не то количество конфет!")
        player_turn(player)


def candy_print(x): return print(f"Конфет осталось - {x}")
def victories(x): return print(f"Победил {x}!")


def candy_game(player_1, player_2):
    clear()
    all_candy = 2021
    first = random.randint(0, 2)
    print(f"Первым ходит {player_1}" if first else f"Первым ходит {player_2}")
    if not player_2 == "Bot":
        while all_candy > 0:
            clear()
            if first:
                candy_print(all_candy)
                all_candy -= player_turn(player_1)
                first = False
            else:
                candy_print(all_candy)
                all_candy -= player_turn(player_2)
                first = True
        if first:
            victories(player_2)
        else:
            victories(player_1)
    else:
        while all_candy > 0:
            if first:
                candy_print(all_candy)
                all_candy -= player_turn(player_1)
                first = False
                clear()
            else:
                candy_print(all_candy)
                all_candy -= bot(all_candy)  
                first = True
        if first:
            victories(player_2)
        else:
            victories(player_1)


def main():
    start()
    mode = game_mode()
    player_1, player_2 = player_name(mode)
    candy_game(player_1, player_2)


clear()
#test_bot()
main()
