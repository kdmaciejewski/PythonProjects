import random as r

if __name__ == '__main__':
    countries = ['Uruguay', 'Russia', 'Saudi Arabia', 'Egypt', 'Spain', 'Portugal', 'Iran', 'Morocco', 'France',
                 'Denmark', 'Peru', 'Australia', 'Croatia', 'Argentina', 'Nigeria', 'Iceland', 'Brazil', 'Switzerland',
                 'Serbia', 'Costa Rica', 'Sweden', 'Mexico',
                 'Korea Republic', 'Germany', 'Belgium', 'England', 'Tunisia', 'Panama', 'Colombia', 'Japan', 'Senegal',
                 'Poland']

    r.shuffle(countries)



    for i in range(8):
        names = {}
        names[chr(r.randint(65, 72))] = countries[r.randint(0, len(countries) - 1)]
        print(names)


