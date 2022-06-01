import datetime
class Logger:
    def __init__(self):
        self.name = "logfiles.txt"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, file_name):
        self.__name = file_name

    def write(self, message):
        text = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " " + message + "\n"
        with open(self.name, "a+") as file:
            file.write(text)