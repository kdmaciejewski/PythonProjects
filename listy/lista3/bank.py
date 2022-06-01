import random
import sys

def log():

   print("Witaj w banku Santander Polska")
   isBad = True

   while isBad:
       try:
           pin = input('Podaj numer PIN ')
           if len(pin) != 4 or not pin.isdigit():
               raise ValueError('Błędnie podany kod PIN')
           else:
               isBad = False

       except ValueError as ve:
           print(ve, sys.exc_info()[0])


   print("Logowanie pomyślne")
   saldo = random.randint(0, 22000)

   while True:

       try:

           op = input("1 - Sprawdzenie salda\n2 - Wypłata gotówki\n3 - Wyjście\n")

           if (op == '1'):
               print('Saldo: ' + str(saldo))
           elif (op == '2'):
               suma = int(input('Podaj sumę do wypłaty '))
               if suma > int(saldo):
                    print("Niewstarczające saldo, nie można zrealizować transakcji")
                    print('Brakuje: ' + str(suma - int(saldo)) + " zł")
               else:
                   saldo -= suma
                   print('Suma została wypłacona')

           elif op == '3':
               print("Pomyślnie wylgogowano z systemu")
               break

           else:
               raise ValueError('Podano złą wartość operacji')

       except ValueError as val:
           print(val, sys.exc_info()[0])


if __name__ == '__main__':
    log()