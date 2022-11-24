from user_interface import *
from reed_data import *
from view_data import *
from search_data import *


def model_constructor():
    start_program()
    data1 = pars_csv_data(reed_persons())
    data2 = pars_csv_data(reed_phone_list())
    data = all_data(data1, data2)
    mode = mode_selection()
    if mode == 1:
        create_new_data(data1)
    elif mode == 2:
        view_data(data)
    elif mode == 3:
        s_mode = mode_search()
        if s_mode == 1:
            second_name = input_search("фамилию")
            id = search_by_second_name(data1, second_name)
            data2 = pars_csv_data(reed_phone_list())
            data = all_data_in_id(id, data1, data2)
            view_data(data)
        elif s_mode == 2:
            name = input_search("имя")
            id = search_by_name(data1, name)
            data2 = pars_csv_data(reed_phone_list())
            data = all_data_in_id(id, data1, data2)
            view_data(data)
        elif s_mode == 3:
            phone = input_search("телефон")
            id = search_by_phone(data2, phone)
            data2 = pars_csv_data(reed_phone_list())
            data = all_data_in_id(id, data1, data2)
            view_data(data)

