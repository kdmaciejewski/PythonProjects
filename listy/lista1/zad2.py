def auto_lights():
    mode = input("Is the automatic mode on? (True/False) ")
    time = input("What's the time? (Day/Night) ")
    weather = input("Is the weather bad? (True/False) ")

    if mode == "True":
        if time == "Night" or weather == "True":
            print('Lights are on')
    else:
        print('Lights are off')


if __name__ == '__main__':
    auto_lights()