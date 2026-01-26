"""
Для таблиці «матеріалу» з завдання 4 створіть користувальницьку агрегатну функцію, яка рахує середнє значення
ваги всіх матеріалів вислідної вибірки й округляє значення до цілого.
"""

import csv


def file_open(file):
    with open(file, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def weight_mean():
    reader = file_open(filename)
    list_weight = []
    for row in reader:
        list_weight.append(float(row['Weight']))
    if not list_weight:
        return 0
    mean = sum(list_weight) / len(list_weight)
    return int(round(mean))


def client_info(identifier, *args):
    reader = file_open(filename)
    result_list = []
    for row in reader:
        if row["Identifier"] == str(identifier):
            for arg in args:
                result_list.append(row[str(arg).lower().capitalize()])
    result = " ".join(result_list)
    return result


filename = "materials.csv"
fieldnames = ["Identifier", "Weight", "Height", "Additional characteristics"]
materials_db = [
    {
        "Identifier": 1,
        "Weight": 150.5,
        "Height": 200.0,
        "Additional characteristics": [("Колір", "Сірий"), ("Тип", "Нержавіюча сталь")]
    },
    {
        "Identifier": 2,
        "Weight": 45.8,
        "Height": 350.5,
        "Additional characteristics": [("Порода", "Дуб"), ("Вологість", "12%"), ("Обробка", "Лак")]
    },
    {
        "Identifier": 3,
        "Weight": 5.8,
        "Height": 100.0,
        "Additional characteristics": [("Матеріал", "Бавовна"), ("Щільність", "Висока")]
    },
    {
        "Identifier": 4,
        "Weight": 12.8,
        "Height": 150.0,
        "Additional characteristics": [("Прозорість", "Так"), ("Міцність", "Загартоване")]
    }
]

with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(materials_db)

print(f"Середня вага: {weight_mean()}")
print(client_info(1, "Weight", "height", "Additional characteristics"))


