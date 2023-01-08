from datetime import datetime, timedelta
#ngay_bat_dau = '2022-12-27'
# arr = ngay_bat_dau.split('-')
# print(arr)
# current_date = datetime(int(arr[0]), int(arr[1]), int(arr[2]))
# next_date = current_date + timedelta(days=1)
# print(next_date)

# next_day_name = next_date.strftime("%A")
# print(next_day_name)

# print(next_date.strftime("%Y-%m-%d"))



# date_time_str = '2022-12-27'

# date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')


# print ("The type of the date is now",  type(date_time_obj))
# print ("The date is", date_time_obj)

#import os, time
#print(time.strftime('%X %x %Z'))
# os.environ['TZ'] = 'Europe/London'
# time.timezone()
# print(time.strftime('%X %x %Z'))

import subprocess
import time

subprocess.call(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"])
time.sleep(3)