import os
def clear(): return os.system('cls')
from reed_data import new_id
from import_data import import_data
from search_data import search_by_names
from import_phone_list import import_phone_list

def start_program():
    clear()
    print("=======================\n" +
          "=Телефонный справочник=\n" +
          "=======================\n")


def mode_selection():
    while True:
        print("(1) запись в базу данных\n" +
              "(2) чтение базы данных\n" +
              "(3) поиск по базе данных")
        mode = int(input("-->"))
        if not (mode == 1 or mode == 2 or mode == 3):
            print("Неверное число!")
        else:
            clear()
            return mode


def create_new_data(data):
    id = new_id(data)
    second_name = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    note = input("Введите заметку: ")
    n_id = search_by_names(data, [second_name, name])
    if new_id != None:
        id = n_id
        import_phone_list(id, phone, note)
    else:
        result = [id, second_name, name, phone, note]
        import_data(result)

def mode_search():
    while True:
        print("(1) поиск по фамилии\n" +
              "(2) поиск по имени\n" +
              "(3) поиск по номеру")
        mode = int(input("-->"))
        if not (mode == 1 or mode == 2 or mode == 3):
            print("Неверное число!")
        else:
            clear()
            return mode


def input_search(text):
    return input(f"Введите {text}: ")

