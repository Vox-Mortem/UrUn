class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        for i in range(1, self.new_floor + 1):
            if 1 <= self.new_floor <= self.number_of_floors:
                print(i)
            else:
                print('"Такого этажа не существует"')
                break

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if type(self.number_of_floors) == type(other.number_of_floors):
            return self.number_of_floors == other.number_of_floors
        else:
            print('Типы исходных данных в EQ не совпадают')

    def __lt__(self, other):
        if type(self.number_of_floors) == type(other.number_of_floors):
            return self.number_of_floors < other.number_of_floors
        else:
            print('Типы исходных данных в LT не совпадают')

    def __le__(self, other):
        if type(self.number_of_floors) == type(other.number_of_floors):
            return self.number_of_floors <= other.number_of_floors
        else:
            print('Типы исходных данных в LE не совпадают')

    def __gt__(self, other):
        if type(self.number_of_floors) == type(other.number_of_floors):
            return self.number_of_floors > other.number_of_floors
        else:
            print('Типы исходных данных в GT не совпадают')

    def __ge__(self, other):
        if type(self.number_of_floors) == type(other.number_of_floors):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('Типы исходных данных в GE не совпадают')

    def __ne__(self, other):
        if type(self.number_of_floors) == type(other.number_of_floors):
            return self.number_of_floors != other.number_of_floors
        else:
            print('Типы исходных данных в NE не совпадают')

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
