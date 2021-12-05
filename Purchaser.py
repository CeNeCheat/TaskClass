customer = []
class Purchaser:
    def __init__(self, name=None, surname=None, creditcard=None):
        self.__name = name
        self.__surname = surname
        self.__creditcard = creditcard
    def printInfo(self):
        print("Фамилия Имя: ", self.__surname, " ", self.__name)
        print("Номер карты: ", self.__creditcard)
pur1 = Purchaser(name=input("Введите имя: "), surname=input("Введите фамилию"), creditcard=input("Введите номер карты: "))
pur2 = Purchaser(name="Григорий", surname="Анатолий", creditcard="0000")
purlist = []
for count in range(2):
    x= pur1()
    x.attr = count
    purlist.append(x)
pur1.printInfo()
pur2.printInfo()
    