import datetime as dt
import time
while True:
    now = dt.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time = ", current_time)
    print("Current hour = ", now.strftime("%H"))
    if int(now.strftime("%H")) > 6:
        print("It's later than 6 o'clock now")
    time.sleep(2.0)
