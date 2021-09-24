import datetime

date = datetime.datetime.now()
print(date) # 2021-09-24 11:22:46.729396
print(date.date()) # 2021-09-24
print(date.time()) # 11:22:46.729396
print(
  date.year, date.month, date.day,
  date.hour, date.minute, date.second, date.microsecond,
  date.weekday(),
  ) 
# 2021 9 24 11 22 46 729396 4

customDate = datetime.datetime(2021, 9, 25)
print(customDate) # 2021-09-25 00:00:00

delta = datetime.timedelta( 
  weeks=1, days=2, hours=2,
  minutes=1, seconds=12, milliseconds=10
  )
print(delta) # 9 days, 2:01:12.010000

zeroDelta = datetime.timedelta()
print(zeroDelta) # 0:00:00

print(customDate - date)
# 12:37:13.270604

print(customDate + delta)
# 2021-10-04 02:01:12.010000
