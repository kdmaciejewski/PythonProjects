import time

def timer(func):
    def wraper():
        print('Obliczanie czasu wykonywania funkcji')
        a = time.perf_counter()
        func()
        b = time.perf_counter()

        print('Upłynęło: ' + str(b-a) + ' sekundy')

    return wraper

@timer
def first():
    suma = 0
    for i in range(20000003):
        suma += 0.2222
    return suma

if __name__ == '__main__':
    #t = timer(first)
    #t()
    first()