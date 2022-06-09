import calendar

print("Введите дату типа 05/2022 ")
def get_last_friday(inputDate):
    f = inputDate.split('/')
    friday = calendar.FRIDAY
    year = int(f[1])
    month = int(f[0])
    d = calendar.monthcalendar(year, month)
    calc_day = d[-1][friday] or d[-2][friday]
    rslt = str(calc_day) + '.' + str(month) + '.' + str(year)
    print(rslt)
    return rslt

get_last_friday(input(str()))
