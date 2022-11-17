from datetime import datetime, date, timedelta

users = [{'name': 'Artur', 'birthday': date(year=1989, month=3, day=14)},
         {'name': 'Abraham', 'birthday': date(year=1998, month=11, day=10)},
         {'name': 'Amber', 'birthday': date(year=1995, month=11, day=7)},
         {'name': 'Kira', 'birthday': date(year=1998, month=11, day=15)},
         {'name': 'Bridjet', 'birthday': date(year=1991, month=10, day=12)},
         {'name': 'Leslie', 'birthday': date(year=1988, month=11, day=24)},
         {'name': 'Caroline', 'birthday': date(year=1991, month=11, day=18)},
         {'name': 'Diego', 'birthday': date(year=1997, month=11, day=18)},
         {'name': 'Carter', 'birthday': date(year=2001, month=12, day=11)},
         {'name': 'Emma', 'birthday': date(year=1991, month=11, day=12)},
         {'name': 'Joseph', 'birthday': date(year=1988, month=11, day=5)},
         {'name': 'Henry', 'birthday': date(year=1991, month=9, day=10)},
         {'name': 'Kevin', 'birthday': date(year=1997, month=11, day=23)},
         {'name': 'Anna', 'birthday': date(year=2001, month=11, day=11)}
         ]

day_list = {'Monday': [],
            'Tuesday': [],         
            'Wednesday': [],
            'Thursday': [],
            'Friday': [],         
            'Saturday': [],
            'Sunday': []
         }

def list_birthday(users : list):

    seventh_day = datetime.now()
    interval = seventh_day + timedelta(weeks=1)
    
    for user in  users:
        year_HB = user.get('birthday') 
        list1 = str(year_HB).split('-')
        this_year = datetime.now().year
        dbtd = datetime(year=int(this_year), month=int(list1[1]), day=int(list1[2]))

        if ( seventh_day < dbtd <= interval ):
            weekday_string = dbtd.strftime("%A")
            if weekday_string in ['Saturday', 'Sunday']:
                weekday_string = 'Monday'
            day_list.get(weekday_string).append(user.get('name'))
            
    return day_list


def zapis(days : dict):  
    with open('output.txt', 'w') as f:
        for key, value in days.items():
            if value:
                d = ', '.join(value)
                f.write(f'{key}: {d}\n')     

if __name__ == '__main__':
    list_birthday(users)
    zapis(day_list)
