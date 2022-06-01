men_names = []
women_names = []

with open("imiona", encoding = 'utf-8') as f:
    direction = False
    temp = f.read().splitlines()
    for i in temp:
        if i == 'Kobiety':
           continue
        elif i == 'Mężczyźni':
            direction = True
        elif direction:
            men_names.append(i)
        else:
            women_names.append(i)


class Controlled_text:
    def __init__(self, text):
        self.text = text

    def __gt__(self, other):
        if (len(self.text) > len(other.text)):
            return True
        else:
            return False

    def __lt__(self, other):
        if (len(self.text) < len(other.text)):
            return True
        else:
            return False

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, val):
        if len(val) >= 1:
            for i in list(val):
                if i.isprintable():
                    if i.isspace():
                        raise ValueError("Char can't be a space")
                    else:
                        self.__text = val
                else:
                    raise ValueError("Char is not printable")

class First_name(Controlled_text):
    def __init__(self, text):
        super().__init__(text)
        self.name = text
    def __repr__(self):
        return f"{self.name}"
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if len(val) >= 1:
            for i in list(val):
                if i.isprintable():
                    if i.isspace():
                        raise ValueError("Char can't be a space")
                else:
                    raise ValueError("Char is not printable")

        val = val.lower()
        val = val.capitalize()

        if val in men_names or val in women_names:
            self.__name = val
        else:
            raise ValueError('Name is not variant')

    def is_male(self, name):
        if name in men_names:
            return True
        return False

    def is_female(self, name):
        if name in women_names:
            return True
        return False

class Last_name(Controlled_text):
    def __init__(self, text):
        super().__init__(text)
        self.lname = text

    def __repr__(self):
        return f"{self.lname}"
    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, val):
        if len(val) >= 1:
            for i in list(val):
                if i.isprintable():
                    if i.isspace():
                        raise ValueError("Char can't be a space")
                else:
                    raise ValueError("Char is not printable")
        tex = val.lower()
        tex = tex.capitalize()
        if not '-' in list(val):
            if tex == val:
                self.__lname = val
        else:
            cond = False
            countUpper = 0

            for i in val:
                if i.isupper():
                    countUpper = countUpper + 1
                if cond:
                    if i.isupper():
                        cond = False
                    else:
                        raise ValueError('Small letter after -')
                if i == '-':
                    cond = True

            if countUpper <= 2:
                self.__lname = val
            else:
                raise ValueError('Too many upper letters')


class Ident_number(Controlled_text):
    def __init__(self, val):
        #super().__init__(val)
        if len(val) == 7:
            count = 0
            for i in list(val):
                if i.isdigit():
                    count = count + int(i)
                else:
                    raise ValueError('Char is not digit')
        a = count % 97
        val = val + str(a)
        self.__text = val

    def __repr__(self):
        return f"{self.text}"
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, val):
        raise AttributeError('Denied')
        # if len(val) == 7:
        #     count = 0
        #     for i in list(val):
        #         if i.isdigit():
        #             count = count + int(i)
        #         else:
        #             raise ValueError('Char is not digit')
        # a = count % 97
        # val = val + str(a)
        # self.__text = val

class Person:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id

    def __repr__(self):
        return f"Person: {self.name}, {self.surname}, {self.id}"
    @classmethod
    def from_string(self, text):
        list = text.split("/; ")
        if len(list) != 3:
            raise ValueError('Wrong number of attributes')
        else:
            return Person(First_name(list[0]), Last_name(list[1]), Ident_number(list[2]))
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if type(val) == First_name:
            self.__name = val
        else:
            raise ValueError('Wrong type of the attribute')
    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, val):
        if type(val) == Last_name:
            self.__surname = val
        else:
            raise ValueError('Wrong type of the attribute')

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, val):
        if type(val) == Ident_number:
            self.__id = val
        else:
            raise ValueError('Wrong type of the attribute')

def test():
    with open("zad5", encoding='utf-8') as f:
        temp = f.read().splitlines()
        for i in temp:
           print(Person.from_string(i))



if __name__ == '__main__':

    c = Controlled_text('ello')
    # c.text = ' '
    c2 = Controlled_text('Krzyszof')
    print(c > c2)
    print(c < c2)
    n = First_name('krzysztof')
    print(n.name)
    print(n.is_male(n.name))
    l = Last_name("Maciejewski-Bąk")
    # l = Last_name('Maciejewski-BAK')

    i = Ident_number('1234567')
    #i.text = '1234567'
    print(i.text)

    p = Person(n, l, i)
    p2 = Person.from_string('Krzysztof/Bąk/1234567')
    print(p2)

    test()

