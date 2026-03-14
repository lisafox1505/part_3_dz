import datetime
import sqlite3

import smtplib
import ssl
from email.message import EmailMessage
from my_pass import app_password, sender_email


def add_data_into_db(data: tuple) -> None:
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    create_table = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    short_name TEXT NOT NULL,
    birthday DATE NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL
    );
    """
    cursor.execute(create_table)
    conn.commit()

    try:
        cursor.execute("INSERT INTO users (full_name, short_name, birthday, age, email) VALUES(?,?,?,?,?)", data)
        conn.commit()
    except sqlite3.Error as error:
        print(f"Помилка баз даних: {error}")
    finally:
        conn.close()


class UserData:
    def __init__(self, first_name: str, last_name: str, middle_name: str, birthday: datetime.date, email: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birthday = birthday
        self.email = email


    def __str__(self) -> str:
        return f"Ім'я: {self.get_full_name()}\nДата народження: {self.birthday}"


    def get_full_name(self) -> str:
        return f"{self.last_name.lower().strip().title()} {self.first_name.lower().strip().title()} {self.middle_name.lower().strip().title()}"


    def get_short_name(self) -> str:
        return f"{self.last_name.lower().strip().title()} {self.first_name[0].title()}. {self.middle_name[0].title()}."


    def get_age(self) -> int:
        now = datetime.date.today()
        result = now.year - self.birthday.year - ((now.month, now.day) < (self.birthday.month, self.birthday.day))
        return result

def send_email(user_email: str, user_name: str) -> None:
    print(f"Кому: {user_email}")
    print(f"Текст: {user_name}, дякуємо за реєстрацію!")
    print("-" * 30)


def send_real_email(user_name: str, user_email: str) -> None:

    msg = EmailMessage()
    msg['Subject'] = "Реєстрація нового користувача"
    msg['From'] = sender_email
    msg['To'] = sender_email
    msg.set_content(
        f"Зареєстровано нового користувача: {user_name}\n"
        f"Пошта користувача: {user_email}\n"
        f"Дата реєстрації: {datetime.date.today()}"
    )

    smtp_server = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
            print(f"Лист успішно надіслано на {sender_email}")
    except Exception as e:
        print(f"Помилка при відправці пошти: {e}")


def register_user(data: UserData) -> None:
    full_name = data.get_full_name()
    short_name = data.get_short_name()
    birthday = str(data.birthday)
    email = data.email
    data = (full_name, short_name, birthday, data.get_age(), email)
    add_data_into_db(data)

    send_email(email, full_name)
    send_real_email(full_name, email)


def user_search(first_name: str, second_name: str, email: str) -> None:
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users "
                       "WHERE full_name LIKE ? "
                       "AND full_name LIKE ? "
                       "AND email = ?",
                       (f"%{first_name.strip().title()}%", f"%{second_name.strip().title()}%", email.strip()))
        print(cursor.fetchall())
    except sqlite3.Error as error:
        print(f"Помилка баз даних: {error}")
    finally:
        conn.close()


if __name__ == "__main__":
    # users_to_add = [
    #     UserData("Олександр", "Петренко", "Іванович", datetime.date(1990, 5, 15), "olex@test.com"),
    #     UserData("Марія", "Коваленко", "Сергіївна", datetime.date(1995, 12, 1), "maria@test.com"),
    #     UserData("Іван", "Бойко", "Миколайович", datetime.date(2000, 1, 10), "vanya@test.com"),
    #     UserData("Ганна", "Лисенко", "Василівна", datetime.date(1988, 8, 24), "hanna@test.com"),
    #     UserData("Дмитро", "Шевченко", "Олегович", datetime.date(2010, 3, 20), "dima@test.com"),
    #     UserData("Сергій", "Ткаченко", "Петрович", datetime.date(1985, 2, 28), "serg@test.com"),
    #     UserData("Наталія", "Кравченко", "Павлівна", datetime.date(1998, 6, 5), "natali@test.com"),
    #     UserData("Андрій", "Мороз", "Вікторович", datetime.date(2005, 9, 14), "andrii@test.com"),
    #     UserData("Юлія", "Клименко", "Олександрівна", datetime.date(1993, 4, 30), "yulia@test.com")
    # ]
    #
    # for user in users_to_add:
    #     register_user(user)

    obj = UserData("Юлія", "Клименко", "Олександрівна", datetime.date(1993, 4, 30), "yulia@test.com")
    register_user(obj)

    user_search(" олександр ", "ПЕТРЕНКО", "olex@test.com")
    user_search("марія", " коваленко", "maria@test.com")