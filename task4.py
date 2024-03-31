from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_to_birthday = (birthday_this_year - today).days

        if 0 <= days_to_birthday <= 7:
            congratulation_date = birthday_this_year

            if birthday_this_year.weekday() in [5, 6]:
                congratulation_date += timedelta(days=7 - birthday_this_year.weekday())

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming_birthdays

if __name__ == "__main__":
    users = [
        {"name": "Jake Smith", "birthday": "1990.03.28"},
        {"name": "Jane Smith", "birthday": "1990.03.29"},
        {"name": "Nick Darsel", "birthday": "1984.03.30"},
        {"name": "John Doe", "birthday": "1985.04.01"},
        {"name": "Ethan Williams", "birthday": "1970.04.02"},
        {"name": "Smith Smith", "birthday": "1990.04.03"},
        {"name": "Liam Smith", "birthday": "1995.04.04"},
        {"name": "Liam Smith", "birthday": "1995.04.05"},
        {"name": "Mohel Smith", "birthday": "1995.04.06"},
        {"name": "John Dark", "birthday": "1985.04.07"},
        {"name": "Mary Dark", "birthday": "1985.04.08"},
        {"name": "Derek Dark", "birthday": "1985.04.09"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
