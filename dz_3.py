from datetime import datetime, date, timedelta
users = [{'name': 'Artur', 'birthday': date(year=1989, month=3, day=14)},
         {'name': 'Abraham', 'birthday': date(year=1998, month=11, day=10)},
         {'name': 'Amber', 'birthday': date(year=1995, month=11, day=7)},
         {'name': 'Kira', 'birthday': date(year=1998, month=11, day=15)},
         {'name': 'Bridjet', 'birthday': date(year=1991, month=10, day=12)},
         {'name': 'Leslie', 'birthday': date(year=1988, month=11, day=14)},
         {'name': 'Caroline', 'birthday': date(year=1991, month=11, day=17)},
         {'name': 'Diego', 'birthday': date(year=1997, month=11, day=18)},
         {'name': 'Carter', 'birthday': date(year=2001, month=12, day=11)},
         {'name': 'Emma', 'birthday': date(year=1991, month=11, day=12)},
         {'name': 'Joseph', 'birthday': date(year=1988, month=11, day=5)},
         {'name': 'Henry', 'birthday': date(year=1991, month=9, day=10)},
         {'name': 'Kevin', 'birthday': date(year=1997, month=11, day=24)},
         {'name': 'Anna', 'birthday': date(year=2001, month=11, day=11)}
         ]
day_list = [{'Monday': None},
            {'Tuesday': None},         
            {'Wednesday': None},
            {'Thursday': None},
            {'Friday': None},         
            {'Saturday': None},
            {'Sunday': None}
         ]

def list_birthday(list : list):

    seventh_day = datetime.now()
    interval = seventh_day + timedelta(weeks=1)
    d0 = []
    d1 = []
    d2 = []
    d3 = []
    d4 = []


    for i in range (len(list)):
        year_HB =list[i].get('birthday') 
        list1= str(year_HB).split('-')
        this_year = datetime.now().year
        dbtd = datetime(year=int(this_year), month=int(list1[1]), day=int(list1[2]))

        if ( seventh_day < dbtd < interval ):
            day = dbtd.weekday()
            if day in (0,5,6):
                d0.append(list[i].get('name'))
            elif day == 1:
                d1.append(list[i].get('name'))
            elif day == 2:
                d2.append(list[i].get('name'))
            elif day == 3:
                d3.append(list[i].get('name'))
            elif day == 4:
                d4.append(list[i].get('name'))
    day_list = [{'Monday': d0},
            {'Tuesday': d1},         
            {'Wednesday': d2},
            {'Thursday': d3},
            {'Friday': d4}         
           
         ]
    return day_list
            
day_list = (list_birthday(users))
with open('output.txt', 'w') as f:
    for i in day_list:
        for key, value in i.items():
            if value:
                d = ', '.join(value)
                f.write(f'{key}: {d}\n')