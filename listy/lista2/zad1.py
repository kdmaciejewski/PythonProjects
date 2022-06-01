import math as m

def count_radians(angle):

    return str((m.pi * angle)/180)

def value():
    print('Wartość radianów dla 360 stopni: ' + count_radians(360))
    print('Wartość z modułu: ' + str(m.radians(360)))

    print('Wartość radianów dla 90 stopni: ' + count_radians(90))
    print('Wartość z modułu: ' + str(m.radians(90)))

    print('Wartość radianów dla 45 stopni: ' + count_radians(45))
    print('Wartość z modułu: ' + str(m.radians(45)))


if __name__ == '__main__':
    value()