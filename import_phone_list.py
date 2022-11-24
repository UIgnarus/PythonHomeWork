
def import_id(data):
    with open("phone_list.csv", "a", encoding="utf-8") as file:
        file.write(f"{data};")


def import_phone(data):
    with open("phone_list.csv", "a", encoding="utf-8") as file:
        file.write(f"{data};")


def import_not(data):
    with open("phone_list.csv", "a", encoding="utf-8") as file:
        file.write(f"{data}\n")


def import_phone_list(id, phone, note):
    import_id(id)
    import_phone(phone)
    import_not(note)
    
