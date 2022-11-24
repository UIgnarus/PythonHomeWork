from import_persons import import_persons
from import_phone_list import import_phone_list


def import_data(data):
    import_persons(data[0], data[1], data[2])
    import_phone_list(data[0], data[3], data[4])


