

class Car:
    def __init__(self, fuel):
        self.__fuel = fuel

    def get_fuel(self):
        return self.__fuel

    def set_fuel(self, number):
        self.__fuel = number
        if self.__fuel == 0:
            return "Значение равно 0"
        elif self.__fuel < 0 :
            return "Значение меньше 0"
        else:
            return self.__fuel


obj2 = Car(90)
print(obj2.get_fuel())
print(obj2.set_fuel(0))
print(obj2.set_fuel(-12))
print(obj2.set_fuel(9))



