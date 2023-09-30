## Dates

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

######
# Name of month
x = datetime.datetime(2019, 6, 1)
print(x.strftime("%B"))


