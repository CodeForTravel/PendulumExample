import pendulum

def new_date_func(args):
    map_datename_to_pendulum = {
        'saturday': pendulum.SATURDAY,
        'sunday': pendulum.SUNDAY,
        'monday': pendulum.MONDAY,
        'tuesday': pendulum.TUESDAY,
        'wednesday': pendulum.WEDNESDAY,
        'thursday': pendulum.THURSDAY,
        'friday': pendulum.FRIDAY,
    }
    date_input = map_datename_to_pendulum.get(args)
    new_date_name = pendulum.now().next(date_input).strftime('%Y-%m-%d')
    return new_date_name
vr = 'friday'
print(new_date_func(vr))