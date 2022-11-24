

def search_by_names(data, names):
    for i in data:
        if i[1] == names[0] and i[2] == names[1]:
            return i[0]
    return None


def search_by_second_name(data, second_name):
    for i in data:
        if i[1] == second_name:
            return i[0]
    return None



def search_by_name(data, name):
    for i in data:
        if i[2] == name:
            return i[0]
    return None


def search_by_phone(data, phone):
    for i in data:
        if i[1] == phone:
            return i[0]
    return None
