#7.
import csv
import json
import os
from xml.etree import ElementTree as ET

file_name = "people_data.csv"

def csv_file_create(act, user_name=None, user_surname=None, user_birthday=None, user_city=None):
    field = ["name", "surname", "birthday", "city"]
    rows = {
        "name": user_name,
        "surname": user_surname,
        "birthday": user_birthday,
        "city": user_city
    }

    file_exists = os.path.isfile(file_name)
    try:
        with open(file_name, act, newline="", encoding="utf-8") as file:
            if act == "r":
                reader = csv.DictReader(file)
                for row in reader:
                    print(row["name"], row["surname"], row["birthday"], row["city"])

            else:
                writer = csv.DictWriter(file, fieldnames=field)

                if act == "a":
                    if not file_exists:
                        writer.writeheader()
                    writer.writerow(rows)
                    return "Дані додано"

                elif act == "w":
                    writer.writeheader()
                    writer.writerow(rows)
                    return "Файл перезаписано"

    except Exception as e:
        print(f"ERROR1: {e}")


def csv_open(file):
    try:
        with open(file, encoding="utf-8", newline="") as f_csv:
            read = csv.DictReader(f_csv)
            data = list(read)
            return data
    except Exception as e:
        print(f"ERROR2: {e}")


def csv_in_json(file):
    reader = csv_open(file)
    if not reader:
        raise ValueError (f"Файл {file} не знайдено")

    try:
        with open("people_data.json", "w", encoding="utf-8") as f_json:
            json.dump(reader, f_json, ensure_ascii=False, indent=4)
        return "Данні збережені у форматі json"

    except Exception as e:
        print(f"ERROR3: {e}")


def csv_in_xml(file):
    reader = csv_open(file)
    if not reader:
        raise ValueError (f"Файл {file} не знайдено")

    root = ET.Element("people")
    count = 0
    for row in reader:
        count += 1
        sub_elem = ET.SubElement(root, "person")
        sub_elem.set("id", f"{count}")
        for key, value in row.items():
            sub_elem_key = ET.SubElement(sub_elem, key)
            sub_elem_key.text = str(value)
    tree = ET.ElementTree(root)
    ET.indent(tree)
    tree.write("people_data.xml", encoding="utf-8", xml_declaration=True)
    return "Данні збережені у форматі xml"


def input_user_data():
    user_name = input("Введіть ім'я: ").strip()
    user_surname = input("Введіть прізвище: ").strip()
    user_birthday = input("Введіть дату народження: ").strip()
    user_city = input("Введіть місто проживання: ").strip()
    return user_name, user_surname, user_birthday, user_city


while True:
    action = input("\nВиберіть дію:\n"
                   "1 - внести нові дані\n"
                   "2 - перезаписати усі дані\n"
                   "3 - подивитись файл\n"
                   "4 - конвертувати у XML\n"
                   "5 - конвертувати у JSON\n"
                   "6 - вихід\n")
    if action == "6":
        break
    match action:
        case "1":
            name, surname, birthday, city = input_user_data()
            print(csv_file_create("a", name, surname, birthday, city))

        case "2":
            name, surname, birthday, city = input_user_data()
            print(csv_file_create("w", name, surname, birthday, city))

        case "3":
            csv_file_create("r")

        case "4":
            try:
                print(csv_in_xml(file_name))
            except Exception as err:
                print(f"ERROR4: {err}")

        case "5":
            try:
                print(csv_in_json(file_name))
            except Exception as err:
                print(f"ERROR5: {err}")

        case _:
            print("Невірний ввод")
