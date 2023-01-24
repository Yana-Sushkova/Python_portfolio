import datetime


def log_cash(rezhim):
    with open("loghandbook.txt", "a", encoding="utf-8") as file:
        file.write(
            f"Режим = {rezhim}. Дата и время запроса: {datetime.datetime.now()} \n")
