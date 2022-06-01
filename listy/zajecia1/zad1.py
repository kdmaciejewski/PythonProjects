import random
import string

def analyze_text(text):
    tab = text.split()
    words = []
    helper = []
    for i in range(len(tab)):
        if tab[i] == 'OCaml':
            words.append(helper)
            print(helper)
            helper = []
        else:
            helper.append(tab[i])


def change(text):

    text = text.replace(',', ';')

    print(text)

def count_aA(text):
    tab = list(text)

    acc_a = 0
    acc_A = 0

    for i in range(len(tab)):
        if tab[i] == 'a':
            acc_a += 1
        if tab[i] == 'A':
            acc_A += 1

    print("Liczba wystąpień litery a: " + str(acc_a))
    print("Liczba wystąpień litery A: " + str(acc_A))

def count_for(text):
    tab = text.split()
    acc = 0
    word = 'for'
    for i in range(len(tab)):
        if str(tab[i]) == word:
            acc += 1

    # for word in tab:
    #     if word == "for":
    #         acc = acc + 1


    print("Liczba wystąpień słowa 'for': " + str(acc))

def unique():
    s = ''.join(random.choices(string.ascii_lowercase, k=12))
    print("Wygenerowane słowo: " + s)
    tab = list(s)
    helper = []
    for i in range(len(tab)):
        w = tab[i]
        if (w in helper):
            index = helper.index(tab[i])
            helper[index+1] += 1
        else:
            helper.append(tab[i])
            helper.append(1)

    l = []
    for i in range(1, len(helper), 2):
        if helper[i] == 1:
            l.append(helper[i-1])

    print(l)




text = "The OCaml toolchain includes an interactive top-level interpreter, a bytecode compiler, an optimizing native code compiler, a reversible debugger, and a package manager (OPAM). OCaml was initially developed in the context of automated theorem proving, and has an outsize presence in static analysis and formal methods software. Beyond these areas, it has found serious use in systems programming, web development, and financial engineering, among other application domains. The acronym CAML originally stood for Categorical Abstract Machine Language, but OCaml omits this abstract machine.[3] OCaml is a free and open-source software project managed and principally maintained by the French Institute for Research in Computer Science and Automation (INRIA). In the early 2000s, elements from OCaml were adopted by many languages, notably F# and Scala."

analyze_text(text)
count_aA(text)
change(text)
count_for(text)
unique()
