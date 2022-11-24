from reed_data import *


data1 = pars_csv_data(reed_persons())
data2 = pars_csv_data(reed_phone_list())
data = all_data(data1, data2)

def view_data(data):
    print("\nid;second_name;name;phone;note")
    for i in data:
        print(*i)
