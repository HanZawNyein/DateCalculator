from datetime import datetime, date
from dateutil import relativedelta

# get two dates\
today = datetime.today()
d1 = today.strftime("%d/%m/%Y")
d2 = '17/5/2002'

# convert string to date object
start_date = datetime.strptime(d1, "%d/%m/%Y")
end_date = datetime.strptime(d2, "%d/%m/%Y")

# Get the relativedelta between two dates
delta = relativedelta.relativedelta(end_date, start_date)
print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')
