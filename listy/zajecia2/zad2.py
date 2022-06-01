import sys

def add(a, b):
    return a + b

def sub(a, b):
    try:
        if b == 0:
            raise ValueError('Wprowadzono złą wartość b')
        else:
            print(a - b)
    except ValueError as val:
        print(val, sys.exc_info()[0])

def div(a, b):
  try:
    print(a/b)

  except ZeroDivisionError as val:
      print(val, sys.exc_info()[0])

def concatenate(a, b):
    foo = '''for i in range(3):
                print(str(a + b + i))'''
    exec(foo)

def helper(a, b, f):
    print(f(a, b))

    try:

        program = input('Wybierz funkcje: (div(a, b), sub(a, b)) ')

        arr2 = list(program)[0:4]
        arr = "".join(arr2)

        if arr == 'div(' or arr == 'sub(':
            exec(program)
        else:
            raise ValueError('Błędnie wprowadzona funkcja')

    except ValueError as val:
        print(val, sys.exc_info()[0])


if __name__ == '__main__':

    a = add
    helper(0, 1, a)