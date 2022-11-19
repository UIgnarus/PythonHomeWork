import os
import random
def clear(): return os.system('cls')


def start():
    clear()
    print("=======================\n" +
          "========28 конфет!=====\n" +
          "=======================\n")


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
    if all_candy > 28:
        result = (all_candy % 29)
        if result == 0:
            result = random.randint(1, 28)
            print(f"Bot выбрал {result}")
            return result
        print(f"Bot выбрал {result}")
        return result
    else:
        print(f"Bot выбрал {all_candy}")
        return all_candy


def test_bot():
    n = 2021
    print(f"\n\nCandy = {n}")
    i = 0
    while n > 0:
        print(f"Bot '{i+1}' = {bot(n)}")
        n -= bot(n)
        print(f"Candy' = {n}")
        i += 1
        i %= 2


def player_turn(player, all_candy):
    while True:
        if all_candy > 28:
            print(f"Ход игрока {player}: ", end="")
            turn = int(input())
            if 1 <= turn <= 28:
                return turn
            else:
                print("Не то количество конфет!")
        else:
            print(f"Ход игрока {player}: ", end="")
            turn = int(input())
            if 1 <= turn <= all_candy:
                return turn
            else:
                print("Не то количество конфет!")


def candy_print(x): return print(f"Конфет осталось - {x}")
def victories(x): return print(f"\n\nПобедил игрок {x}!")


def goes_first(player_1, player_2):
    while True:
        print("Выберите кто ходит первый!\n"
              + f"(1) - игрок {player_1}\n"
              + f"(2) - игрок {player_2}\n"
              + "(3) - Рандом\n")
        turn = int(input("-->"))
        if 1 <= turn <= 3:
            return turn
        else:
            print("Не то количество конфет!")


def candy_game(player_1, player_2):
    clear()
    all_candy = 229
    first = goes_first(player_1, player_2)
    clear()
    if first == 3:
        first = random.randint(0, 1)
    else:
        first %= 2
    print(f"Первым ходит {player_1}" if first
          else f"Первым ходит {player_2}")
    if not player_2 == "Bot":
        while all_candy > 0:
            print("\n")
            if first:
                candy_print(all_candy)
                all_candy -= player_turn(player_1, all_candy)
                first = False
            else:
                candy_print(all_candy)
                all_candy -= player_turn(player_2, all_candy)
                first = True
        if first:
            victories(player_2)
        else:
            victories(player_1)
    else:
        while all_candy > 0:
            print("\n")
            if first:
                candy_print(all_candy)
                all_candy -= player_turn(player_1, all_candy)
                first = False
                
            else:
                clear()
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
    clear()
    player_1, player_2 = player_name(mode)
    candy_game(player_1, player_2)


clear()
test_bot()
#main()
