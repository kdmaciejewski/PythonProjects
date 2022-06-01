def prime(list):

    for i in range(len(list)):
        isPrime = True
        num = list[i]

        if num > 1:
            dzielniki = []
            for j in range(2, int(num/2)):
                if (num % j) == 0:
                    isPrime = False
                    break

            if isPrime:
                print(f"{list[i]} jest liczbą pierwszą")
            else:
                print(f"{list[i]} nie jest liczbą pierwszą")

                for j in range(1, num+1):
                    if (num % j) == 0:
                        dzielniki.append(j)
                print("Jej dzielniki to: ")
                for j in range(len(dzielniki)):
                    print(dzielniki[j], end=" ")
                print()


def sortRosnaco(list):
    list.sort(reverse=False)
    print(list)


def sortMalejaco(list):
    list.sort(reverse=True)
    print(list)


def sortThree(list):
    helper = list[0:3]
    helper.sort()
    for i in range(3):
        list[i] = helper[i]

    print(list)


if __name__ == '__main__':
    list = [19, 3, 15, 43, 98, 16, 9, 23, 4]
    prime(list.copy())
    sortRosnaco(list.copy())
    sortMalejaco(list.copy())
    sortThree(list.copy())