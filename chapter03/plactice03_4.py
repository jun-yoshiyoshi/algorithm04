import time
import datetime

today = datetime.date.today()
_day = datetime.date(1970, 1, 1)

now_time1 = datetime.datetime.now()
now_time2 = time.time()

print(_day)
print(today)
print(now_time1)
print(now_time2)
