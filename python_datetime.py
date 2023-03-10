# -*- coding: utf-8 -*-
"""python datetime.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1txBxgtFyiUWY1kvWn2rKwctiAXPOGPIj
"""

import datetime

print ('the date today is:',datetime.datetime.today())

date_today=datetime.date.today()
print(date_today)

print('this year:',date_today.year)

print('this month:',date_today.month)

print('month name:',date_today.strftime('%B'))

print('date is:',date_today.day)

print("weekday is:",date_today.strftime('%A'))

import datetime

"""###find the date and time difference

"""

import datetime
day1=datetime.date(2018,2,12)

print('day2:',day2.ctime())
print('diff between two dates:',day2-day1)
day_today=datetime.date.today()
print(day_today)
#create delta of four days
no_of_days= datetime.timedelta(days=4)
before_four_days=(day_today- no_of_days)
print("before_four_days:",before_four_days)
after_four_days=(day_today+no_of_days)
print("after_four_days:",after_four_days)

"""###comparision of the date

"""

import datetime
day4=datetime.date.today()
print("today date:",day4)
no_of_days=datetime.timedelta(days=4)
before_four_days= day4 - no_of_days
print("before_four_days:",before_four_days)
after_four_days= day4 + no_of_days
print("after_four_days:",after_four_days)