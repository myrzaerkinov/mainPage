import calendar
from datetime import datetime
day_off = '2022-04-05'
day = datetime.strptime(day_off, "%Y-%m-%d")
print(day.day)
# date = datetime.now()
# for i in range(1, calendar.monthrange(date.year, date.month)[1]+1):
#     if int(day_off) == datetime.strptime(f'{date.year}-{date.month}-{i}', "%Y-%m-%d").weekday():
#         print(datetime.strptime(f'{date.year}-{date.month}-{i}', "%Y-%m-%d").weekday())



# print(date)