from datetime import date
day_month = input().split(' ')
day1 = day_month[0]
month1 = day_month[1]
day_month_year = input().split(' ')
day2 = day_month_year[0]
month2 = day_month_year[1]
year2 = day_month_year[2]
l_date = date(int(year2), int(month2), int(day2))
f_date = date(int(year2), int(month1), int(day1))
delta = f_date - l_date
print(delta.days)