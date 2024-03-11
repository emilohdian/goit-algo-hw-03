from datetime import datetime

def get_days_from_today(date_string):
    try:
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        today = datetime.today()
        difference = today - date_object
        return difference.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."
    
date_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
days_difference = get_days_from_today(date_input)
print("Кількість днів між введеною датою та сьогоднішньою:", days_difference)
