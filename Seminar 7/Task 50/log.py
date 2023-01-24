import datetime


def log_cash(some_str, result):
    with open("logcalc.txt", "a", encoding="utf-8") as file:
        file.write(f"{some_str}= {result}. Время запроса: {datetime.datetime.now()} \n")