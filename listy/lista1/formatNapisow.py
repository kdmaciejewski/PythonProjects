
if __name__ == '__main__':
    # first_message = "Processing file %s"           #literał %s  - ciąg znaków
    # print(first_message % ("file_1.txt"))
    # second_message = "File %s has size %d KB"      #literał d  - liczba digit
    # print(second_message % ("file_1.txt", 100))    #Proszę przeanalizować ten przykład dla A. Zamiany kolejności danych oraz B. Zapisania zamiast 100 -> "100". Przeanalizuj wyniki.
    # third_message = "File %15s has size %10d KB"   #Wartości wprowadzone pomiędzy %, a s lub d - informuje ile znaków ma być zarezerwowane na napis i na wartość liczbową.
    # print(third_message % ("file_1.txt", 100))     #Notacja przydatna szczególnie podczas pracy z plikami. Gdy chce umieścić nazwy mniej więcej w jednym słupku.
    #
    # first_message ="Processing fileeeee {0:s}"         #Ta notacja informuje nas, że mamy wstawić dokładnie jeden parametr i ma on typ str.
    # print(first_message.format("file_1.txt"))
    # second_message = "File {0:s} has size {1:d} KB)" #Dwa parametry - przeanalizuj bazując na poprzednich przykładach.
    # print(second_message.format("file_1.txt", 100))
    # second_message = "File {1:s} has size {0:d} KB)" #Dwa parametry - przeanalizuj bazując na poprzednich przykładach.
    # print(second_message.format(100, "file_1.txt"))
    # third_message = "File {0:15s} has size {1:10d}"   #Analogicznie jak w poprzednim przypadku, umieszczenie wartości liczbowej przez s lub d powoduje zarezerwowanie okreslonej ilości znaków.
    # print(third_message.format("file_1.txt", 100))
    #
    # first_number = 1               #Typ int opisuje liczby całkowite (ujemne oraz dodatnie)
    # type(first_number)
    # second_number = 5.5            #Typ float opisuje liczby zmiennoprzecinkowe
    # type(second_number)
    # type(first_number * second_number)
    # type(first_number / 2)         #Przeanalizuj wynik koncentrując się na operatorze dzielenia.
    # type(first_number // 2)        #Przeanalizuj wynik koncentrując się na operatorze dzielania. - tzw. dzielenie całkowite
    # first_number / 2               #Przeanalizuj wynik dzielnia
    # first_number // 2              #Przeanalizuj wynik dzielnia - zwróć uwagę na zaokrąglenie - dla jakich przypadku może my stosować oba typy dzielenia?
    # type(first_number * second_number)  #Przeanalizuj jaki typ otrzymano w wyniku przeprowadzenia tego działania
    # 5 % 3                          #Modulo - zwraca resztę z dzielenia 5 przez 3
    # float('inf')                   #Zastanów się czy takie rzutpwanie ma sens?
    # float('inf') > 999999999999999999999999999999999999999999999999999999     #Sprawdź wynik porównania.
    # - float('inf')     #Operacja - nieskończonosć (infinity)

    # Indeksowanie elementów
    countries = ['PL', 'DE', 'BE', 'FR', 'US']
    print(countries[:])
    print(countries[1:3])