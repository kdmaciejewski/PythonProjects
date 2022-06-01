def pack(list):
    #sortuje liste a potem biore od początku i końca dopóki nie zapełnie całej
    list.sort()
    bus = 0
    pre = 0

    while bus < 100:
        if len(list) == 0:
            break

        pre = bus
        bus += list.pop(0)

        if bus > 100:
            break

        pre = bus
        bus += list.pop(len(list)-1)

    print('Udało się zapakować: ' + str(pre))


if __name__ == '__main__':
    list = [12, 5, 8, 8, 23, 15, 7, 8, 9, 12, 34, 6, 9, 16, 8, 23, 12, 7, 5, 3]
    pack(list)
