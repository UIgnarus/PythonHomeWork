

def import_id(data):
    with open("persons.csv", "a", encoding="utf-8") as file:
        file.write(f"{data};")


def import_second_name(data):
    with open("persons.csv", "a", encoding="utf-8") as file:
        file.write(f"{data};")


def import_name(data):
    with open("persons.csv", "a", encoding="utf-8") as file:
        file.write(f"{data}\n")


def import_persons(id, second_name, name):
    import_id(id)
    import_second_name(second_name)
    import_name(name)
