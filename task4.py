from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
  today = datetime.today().date()
  upcoming_birthdays = []

  for user in users:
    birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
    birthday_next_year = birthday_this_year.replace(year=today.year + 1)

    if birthday_this_year < today:
      birthday = birthday_next_year

    days_to_birthday = (birthday - today).days

    if 0 <= days_to_birthday <= 7:
      congratulation_date = birthday

      if birthday.weekday() in [5, 6]:
        congratulation_date += timedelta(days=7 - birthday.weekday())

      upcoming_birthdays.append({
          "name": user["name"],
          "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
      })

  return upcoming_birthdays

if __name__ == "__main__":
  users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Mike Jones", "birthday": "1995.02.05"},
  ]

  upcoming_birthdays = get_upcoming_birthdays(users)
  print("Список привітань на цьому тижні:", upcoming_birthdays)