import calendar
import sqlite3
from datetime import date

conn = sqlite3.connect("test.db")
cursor = conn.cursor()


def month_sum(name_column):
    try:
        year = int(input("Enter year: "))
        if year < 1900 or year > 2026:
            print("Invalid Year")
            return month_sum(name_column)

        month = int(input("Enter month: "))
        if month < 1 or month > 12:
            print(f"Invalid Month")
            return month_sum(name_column)

    except ValueError:
        print("Please enter a valid number")
        return month_sum(name_column)

    else:
        days_in_month = calendar.monthrange(year, month)[1]
        start_date = date(year, month, 1)
        end_date = date(year, month, days_in_month)

        query = None
        if name_column == "income":
            query = cursor.execute("SELECT sum(income) FROM expense_table WHERE transaction_time BETWEEN ? AND ?",
                               (str(start_date), str(end_date)))
        elif name_column == "expense":
            query = cursor.execute("SELECT sum(expense) FROM expense_table WHERE transaction_time BETWEEN ? AND ?",
                                   (str(start_date), str(end_date)))
        result = query.fetchone()
        result_suma = result[0]
        if result_suma is None:
            return f"There was no {name_column} this month"

        return f"Monthly {name_column}: {result[0]}\n"


while True:
    action = input("Press ENTER to exit!\n"
                   "Or select action to continue:\n"
                   "1 - Enter expense amount\n"
                   "2 - Enter income amount\n"
                   "3 - Monthly expenses\n"
                   "4 - Monthly income\n")

    if action == "":
        conn.close()
        break

    match action:
        case "1":
            try:
                suma = float(input("Enter suma: "))
                purpose = input("Enter purpose: ")
                cursor.execute("INSERT INTO expense_table (purpose,expense) VALUES (?,?)", (purpose,suma))
                conn.commit()
                print("Data added\n")

            except sqlite3.IntegrityError as e:
                print(f"ERROR:{e}\n")

            except ValueError as e:
                print(f"ERROR:{e}\n")

        case "2":
            try:
                suma = float(input("Enter suma: "))
                cursor.execute("INSERT INTO expense_table (income) VALUES (?)", (suma, ))
                conn.commit()
                print("Data added\n")

            except sqlite3.IntegrityError as e:
                print(f"ERROR:{e}\n")

            except ValueError as e:
                print(f"ERROR:{e}\n")

        case "3":
            try:
                print(month_sum("expense"))
            except sqlite3.Error as e:
                print(f"ERROR:{e}\n")

        case "4":
            try:
                print(month_sum("income"))
            except sqlite3.Error as e:
                print(f"ERROR:{e}\n")

        case _:
            print("Action Error!")