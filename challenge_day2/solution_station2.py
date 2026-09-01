import datetime

def weekday_from_date(year, month, day):
    if datetime.date(year=year,month=month,day=day).weekday() == 0:
        return print('月曜日')
    elif datetime.date(day=day, month=month, year=year).weekday() == 1:
        return print('火曜日')
    elif datetime.date(day=day, month=month, year=year).weekday() == 2:
        return print('水曜日')
    elif datetime.date(day=day, month=month, year=year).weekday() == 3:
        return print('木曜日')
    elif datetime.date(day=day, month=month, year=year).weekday() == 4:
        return print('金曜日')
    elif datetime.date(day=day, month=month, year=year).weekday() == 5:
        return print('土曜日')
    elif datetime.date(day=day, month=month, year=year).weekday() == 6:
        return print('日曜日')
    
print(weekday_from_date(2023,5,12))