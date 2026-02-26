import time
import re
import threading
import os

event = threading.Event()
def reed_file(filename):
    while True:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = f.read()
                res = re.findall(r"Wow!", data)
                if res:
                    event.set()
                    break
                else:
                    time.sleep(5)
                    continue

        except FileNotFoundError:
            time.sleep(5)
            continue


def waiting_for_event(filename):
    event.wait()
    if os.path.isfile(filename):
        os.remove(filename)
        print("Файл видалено!")
    else:
        print("Помилка виконання! Файл не знайден!")

def main(filename):
    thread_1 = threading.Thread(target=reed_file, args=(filename,))
    thread_2 = threading.Thread(target=waiting_for_event, args=(filename,))
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()

main("wowfile.txt")