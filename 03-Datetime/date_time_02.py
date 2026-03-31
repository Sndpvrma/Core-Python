import datetime
today = datetime.date.today()

future = today + datetime.timedelta(days=7)
past = today - datetime.timedelta(days=7)

print("7 days later:",future)
print("7 days ago:",past)
print(today)

import datetime
dob = datetime.date(2004,4,13)
today = datetime.date.today()

age = today.year - dob.year
if(today.month , today.day) < (dob.month , dob.day):
    age -=1
print("your age is :",age)

import datetime
d = datetime.datetime.now()
print("Current hour is:",d)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)
