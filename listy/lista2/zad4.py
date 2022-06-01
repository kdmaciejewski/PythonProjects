import random


def lotto():
    results = []
    player = []
    for i in range(6):
        re = random.randint(1, 49)

        while re in results:
            re = random.randint(1, 49)

        results.append(re)

        pl = random.randint(1,49)

        while pl in results:
            pl = random.randint(1, 49)

        player.append(pl)

    print(results)
    print(player)
    count = 0

    for p in player:
        if p in results:
            count += 1

    print("Liczba trafionych:" + str(count))

if __name__ == '__main__':
    lotto()