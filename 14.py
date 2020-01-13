class Car:
    def __init__(self, number='', model=''):
        self.number = number
        self.model = model

    def __str__(self):
        return "|" + self.number + " " + self.model + '|'

    def __eq__(self, other):
        return self.number == other.number


class Parking:
    def __init__(self, places_count=10):
        self.EMPTY_CAR = Car()
        self.places = [Car()] * places_count

    def park(self, car):
        pos = -1
        for i in range(len(self.places)):
            if self.places[i] == self.EMPTY_CAR:
                pos = i
                break
        if pos != 1:
            self.places[pos] = car
        else:
            print('Parking is full')

    def leave(self, car):
        try:
            pos = self.places.index(car)
            self.places[pos] = self.EMPTY_CAR
        except ValueError:
            print("Car is not founded")

    def __str__(self):
        return ', '.join([str(car) for car in self.places])

    def free(self):
        return self.places.count(Car())


bmw = Car("a123aa", "BMW")
print(bmw)
bmw1 = Car("a123aa", "BMW")
print(bmw == bmw1)
audi = Car('c234cc', "audi")
garage = Parking()
print(garage)
garage.park(bmw)
garage.park(audi)
