import datetime as dt
import time
import calendar


time_now = time.time()
datetime_now = dt.datetime.now(dt.timezone.utc)

epoch =  datetime_now - dt.timedelta(seconds=time_now)
print(epoch)

c = calendar.Calendar()
print(list(c.itermonthdates(2019, 2)))

print(list(d for d in c.itermonthdates(2019, 2) if d.month == 2))
