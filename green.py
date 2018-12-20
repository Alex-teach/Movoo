import datetime
import os
import random

def modify():
    file = open('zero.md', 'r')
    flag = file.readline() == '0'
    file.close()
    file = open('zero.md', 'w+')
    if flag:
        file.write('1')
    else:
        file.write('0')
        file.close()


def commit():
    os.system('git commit -a -m test_github')


def set_sys_time(day, month, year):
    os.system('date %02d%02d1720%04d' % (month, day, year))


def trick_commit(year, month, day):
    set_sys_time(year, month, day)
    modify()
    commit()


def daily_commit(start_date, end_date):
    count = 0
    while (count < 2):
        for i in range((end_date - start_date).days - 5):
            if (i%random.randint(1,2)):
                cur_date = start_date + datetime.timedelta(days=(i+random.randint(1,5)))
                trick_commit(cur_date.day, cur_date.month, cur_date.year)
        count = count + 1


if __name__ == '__main__':
    daily_commit(datetime.date(2016, 7, 29), datetime.date(2018, 1, 9))