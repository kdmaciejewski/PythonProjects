import random

znaki = ['trefl', 'karo', 'kier', 'pik']
figury = ['as', 'król', 'królowa', 'jopek', '10', '9']
kombinacje = []

def tasowanie():

   for f in figury:
       for z in znaki:
           kombinacje.append((f, z))

   print('Wyświetlanie wszystkich kombinacji')
   print(kombinacje)

   random.shuffle(kombinacje)
   gracz_1 = []
   gracz_2 = []

   k = kombinacje.copy()

   for i in range(5):
       gracz_1.append(k.pop())
       gracz_2.append(k.pop())

   print('Talia graczy z pierwszej częśći zadania')
   print(gracz_1)
   print(gracz_2)

def rozgrywka():
    gracz_1 = []
    gracz_2 = []
    cards = {}
    w = 14

    for f in figury:
       cards[f] = w
       w -= 1

    print('Wyświetlanie słownika figur')
    print(cards)

    while len(kombinacje) != 0:
        gracz_1.append(kombinacje.pop()[0])
        gracz_2.append(kombinacje.pop()[0])

    print('Talie graczy w drugiej części rozgrywki')
    print(gracz_1)
    print(gracz_2)

    j = 0

    while len(gracz_1) != 0 or len(gracz_2) != 0:
        k1 = gracz_1.pop()
        k2 = gracz_2.pop()

        w1 = cards[k1]
        w2 = cards[k2]

        if w1 == w2:
           # x = random.randint(0,len(gracz_1)-1)
            #gracz_1.insert(x, k1)
            gracz_1.append(k1)
            gracz_2.append(k2)

        elif w1 > w2:
            x = random.randint(0,len(gracz_1)-1)

            gracz_1.insert(x, k1)
            gracz_1.append(k2)

        else:
            x = random.randint(0,len(gracz_2)-1)

            gracz_2.insert(x, k1)
            gracz_2.append(k2)
        j += 1

        if j == 200:
            break

    if len(gracz_1) < len(gracz_2):
        print('Wygrał gracz 2')

    else:
        print('Wygrał gracz 1')


if __name__ == '__main__':
    tasowanie()
    rozgrywka()