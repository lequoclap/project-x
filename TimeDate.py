__author__ = 'dimage01'

import calendar
import time
import datetime


timer = time.time();

print time

localtime = time.localtime(timer)

print type(localtime)


a  = time.asctime(localtime)
print(a)


calendar = calendar.month(2015,6)

print  calendar

now = datetime.datetime.now()

print(now.microsecond)