import time

t1 = time.time()
print(t1) # 1632463202.4132566

t2 = time.ctime(60*60*24)
print(t2) # Fri Jan  2 05:00:00 1970

# Count a real time sleep
tstart = time.time()
time.sleep(5)
tstop = time.time() - tstart
print(tstop) # 5.006918668746948

t3 = time.gmtime(t1)
print(t3)
# time.struct_time(
# tm_year=2021, tm_mon=9, tm_mday=24,
#  tm_hour=6, tm_min=3, tm_sec=30,
#  tm_wday=4, tm_yday=267, tm_isdst=0)

t4 = time.mktime(t3)
print(t4) # 1632445410.0

t5 = time.asctime(t3)
print(t5) # Fri Sep 24 06:03:30 2021
