from datetime import date
import calendar
day_month = input().split(' ')
day1 = day_month[0]
month1 = day_month[1]
day_month_year = input().split(' ')
day2 = day_month_year[0]
month2 = day_month_year[1]
year2 = day_month_year[2]
leap_year_l = year2
leap_year_h = year2
flag= False
if day1 == '29' and month1 == '02':
    for i in range(4):
        if calendar.isleap(int(leap_year_l)) == False:
            leap_year_l = int(leap_year_l) - 1
    for i in range(4):
        if calendar.isleap(int(leap_year_h)) == False:
            leap_year_h = int(leap_year_h) + 1
    flag = True
if flag == True:
    l_date = date(int(year2), int(month2), int(day2))
    f_date = date(int(leap_year_h), int(month1), int(day1))
else:
    l_date = date(int(year2), int(month2), int(day2))
    f_date = date(int(year2), int(month1), int(day1))
delta = f_date - l_date
print(delta.days)