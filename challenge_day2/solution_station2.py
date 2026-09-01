import datetime
def solution_station_2(date_str):
    year, month, day = map(int, date_str.split('-'))

    if datetime.date(year=year,month=month,day=day).weekday() == 0:
        return ('月曜日') 
    elif datetime.date(day=day, month=month, year=year).weekday() == 1:
        return ('火曜日')
    elif datetime.date(day=day, month=month, year=year).weekday() == 2:
        return ('水曜日')
    elif datetime.date(day=day, month=month, year=year).weekday() == 3:
        return ('木曜日')
    elif datetime.date(day=day, month=month, year=year).weekday() == 4:
        return ('金曜日')
    elif datetime.date(day=day, month=month, year=year).weekday() == 5:
        return ('土曜日')
    elif datetime.date(day=day, month=month, year=year).weekday() == 6:
        return ('日曜日')
