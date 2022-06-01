import datetime as dt


def how_many_days():
    d1 = dt.date.today()
    d2 = dt.date(2022, 12, 31)

    print('Do końca roku pozostało: ' + str((d2 - d1).days) + ' dni')

def how_many_exact():
    print(dt.datetime.now())

    d1 = dt.datetime.today()
    d2 = dt.datetime(2022, 12, 31, 23, 59, 59)
    print('Do końca roku pozostało dokładnie: ' + str(d2 - d1))
if __name__ == '__main__':
    how_many_days()
    how_many_exact()