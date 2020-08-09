import pendulum

date = pendulum.parse('2015-11-5', strict=False)
print('A Random date : '+str(date))


print('date.year : '+str(date.year))
print('date.month : '+str(date.month))
print('date.day : '+str(date.day))
print('date.hour : '+str(date.hour))
print('date.minute : '+str(date.minute))
print('date.day_of_week : '+str(date.day_of_week))
print('date.day_of_year : '+str(date.day_of_year))
print('date.week_of_month : '+str(date.week_of_month))
print('date.week_of_year : '+str(date.week_of_year))
print('date.days_in_month : '+str(date.days_in_month))
print('date.timestamp : '+str(date.timestamp))
print('date.year : '+str(date.year))
print('Canculate Birth Day :'  +str(pendulum.datetime(1998,12,31).age))

print(pendulum.datetime(2020,4,11, tz='Asia/Dhaka').is_dst())
print(pendulum.now('Asia/Dhaka').is_local())
data = "FRIDAY"
next_date = pendulum.now().next(pendulum.FRIDAY).format('YYYY-MM-DD')
print(next_date)
next_date1 = next_date = pendulum.now()

next_date1 = next_date1.next().day_of_week(1)
print(next_date1)