def paragon():
    print('Product  Amount  Vat      Price')

    print('{0:7s}  {1:6d}  {2:3d}      {3:5d}'.format("Bread", 2, 8, 5))

    mess = '%7s  %6d  %3d      %5d'
    print(mess % ("Apple", 22, 19, 1))

    print('{0:7s}  {1:6d}  {2:3d}      {3:5d}'.format("Petrol", 44, 23, 250))

    print('{0:7s}  {1:6d}  {2:3d}      {3:5d}'.format("Bike", 1, 19, 10000))

    print('{0:7s}  {1:6d}  {2:3d}      {3:5d}'.format("Sausage", 3, 8, 15))

    print('{0:7s}  {1:6d}  {2:3d}      {3:5d}'.format("Juice", 2000, 19, 50000))


if __name__ == '__main__':
    paragon()