
def reed_persons():
    with open("persons.csv", "r", encoding="utf-8") as file:
        data = file.read().split("\n")
        data.pop()
    return data

def reed_phone_list():
    with open("phone_list.csv", "r", encoding="utf-8") as file:
        data = file.read().split("\n")
        data.pop()
    return data


def pars_csv_data(data):
    result = []
    for item in data:
        element = item.split(";")
        result.append(element)
    return result


def all_data(p, pl):
    result = []
    for i in p:
        id = i[0]
        for j, item in enumerate(pl):
            element = [i[0], i[1], i[2]]
            if item[0] == id:
                pl.pop(j)
                element.append(item[1])
                element.append(item[2])
                result.append(element)
    return result


def all_id(data):
    result = []
    for i in data:
        result.append(i[0])
    return result


def all_second_name(data):
    result = []
    for i in data:
        result.append(i[1])
    return result


def all_name(data):
    result = []
    for i in data:
        result.append(i[2])
    return result


def all_phones(data):
    result = []
    for i in data:
        result.append(i[1])
    return result


def all_note(data):
    result = []
    for i in data:
        result.append(i[2])
    return result


def all_data_in_id(s_id, data1, data2):
    result = []
    for i in data1:
        id = i[0]
        if id in s_id:
            for j, item in enumerate(data2):
                element = [i[0], i[1], i[2]]
                if item[0] == id:
                    data2.pop(j)
                    element.append(item[1])
                    element.append(item[2])
                    result.append(element)
    return result

def new_id(data1):
    data = all_id(data1)
    if data == []:
        return "1"
    else:
        return str(int(data[-1]) + 1)

    

