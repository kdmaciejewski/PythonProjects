import random
import sys

class User:
    def __init__(self, imie, pin):
        self.setImie(imie)
        self.__imie = imie
        self.setPin(pin)
        self.__pin = pin
        r = random.randint(0, 22000)
        self.setSaldo(r)
        self.__saldo = r

    def setImie(self, imie):
        if isinstance(imie, str):
            self.__imie = imie
        else:
            raise TypeError('The attribute must be a string.')


    def setPin(self, pin):
        if isinstance(pin, str):
            if len(pin) == 4:
                self.__pin = pin
            else:
                raise ValueError('The attribute must have length equal to 4.')
        else:
            raise TypeError('The attribute must be a string.')


    def setSaldo(self, saldo):
        if isinstance(saldo, (int, float)):
            if saldo >= 0 and saldo < 1000000:
                self.__saldo = saldo
            else:
                raise ValueError('The attribute must be positive.')
        else:
            raise TypeError('The attribute must be an int or a float.')

    def getImie(self):
        return self.__imie

    def getPin(self):
        return self.__pin

    def getSaldo(self):
        return self.__saldo


class Bank:

    def log(self):

       print("Witaj w banku Santander Polska")
       isBad = True
       user1 = User("Krzysztof", '0000')

       pin = ''
       while isBad:
           try:
               pin = input('Podaj numer PIN ')
               if len(pin) != 4 or not pin.isdigit():
                   raise ValueError('Błędnie podany kod PIN')
               else:
                   isBad = False

           except ValueError as ve:
               print(ve, sys.exc_info()[0])

       if user1.getPin() == pin:
           print("Logowanie pomyślne")


       #saldo = random.randint(0, 22000)

       while True:

           try:

               op = input("1 - Sprawdzenie salda\n2 - Wypłata gotówki\n3 - Wyjście\n")

               if (op == '1'):
                   print('Saldo: ' + str(user1.getSaldo()))
               elif (op == '2'):
                   suma = int(input('Podaj sumę do wypłaty '))
                   if suma > int(user1.getSaldo()):
                        print("Niewstarczające saldo, nie można zrealizować transakcji")
                        print('Brakuje: ' + str(suma - int(user1.getSaldo())) + " zł")
                   else:
                       user1.setSaldo(user1.getSaldo() - suma)
                       print('Suma została wypłacona')

               elif op == '3':
                   print("Pomyślnie wylgogowano z systemu")
                   break

               else:
                   raise ValueError('Podano złą wartość operacji')

           except ValueError as val:
               print(val, sys.exc_info()[0])


if __name__ == '__main__':
    bank = Bank()
    bank.log()