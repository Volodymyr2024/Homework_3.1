import datetime as dt
from datetime import datetime as dtdt

test = "2020-10-09"

def get_days_from_today(date):
    day_now = dtdt.now() #получаем севоднюшнюю дату
    date_obgekt = dtdt.strptime(date, "%Y-%m-%d") #переводем полученую строку в строку типа dt
    days_betwen = (day_now - date_obgekt).days() # получаем разницу между датами в днях
    print("hey")
    return int(days_betwen)

if __name__ == "__main__":
    get_days_from_today()

