from datetime import datetime

def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        return int((date - datetime.now().date()).days)
    except ValueError:
        print("Неправильний формат дати")

print(get_days_from_today("2025-10-30"))