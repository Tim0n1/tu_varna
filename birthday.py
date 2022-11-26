from datetime import datetime


def get_user_birthday():
    year = int(input())
    month = int(input())
    day = int(input())

    birthday = datetime(2000 + year, month, day)
    return birthday


def calculate_dates(original_date, now):
    delta1 = datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime(now.year + 1, original_date.month, original_date.day)

    return ((delta1 if delta1 > now else delta2) - now).days


bd = get_user_birthday()
now = datetime.now()
c = calculate_dates(bd, now)
print(c)