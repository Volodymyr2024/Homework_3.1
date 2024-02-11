import datetime as dt
from datetime import datetime as dtdt

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthday(users):
    today_date = dtdt.today().date()
    birthdays = []
    for user in users:
        birth_day = user["birthday"]
        birth_day = str(today_date.year) + birth_day[4:]
        birth_day = dtdt.strptime(birth_day, "%Y.%m.%d").date()
        week_day = birth_day.isoweekday()
        days_between = (birth_day - today_date).days

        if 0 <= days_between < 7:
            if week_day < 6:
                birthdays.append({"name": user["name"], "birthday": birth_day.strftime("%Y.%m.%d")})
            else:
                if (birth_day + dt.timedelta(days=1)).weekday() == 0:
                    birthdays.append({"name": user["name"], "birthday": (birth_day + dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                elif (birth_day + dt.timedelta(days=2)).weekday() == 0:
                    birthdays.append({"name": user["name"], "birthday": (birth_day + dt.timedelta(days=2)).strftime("%Y.%m.%d")})
    
    return birthdays

if __name__ == "__main__":
    get_upcoming_birthday()

    