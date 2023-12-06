"""A Object Orientated Programming project for practice by L. Jefferson II, Menoko OG 11/2023, it is a program to demonstrate trains that pick up and drop of cars and an object manager to keep track of number of cars at any given moment."""
class Car:
    def __init__(self, car_id, source, destination):
        self.car_id = car_id
        self.source = source
        self.destination = destination

class Train:
    def __init__(self, train_id, capacity):
        self.train_id = train_id
        self.capacity = capacity
        self.cars = []
    
    def pick_up(self, car):
        if len(self.cars) < self.capacity:
            self.cars.append(car)
            print(f"Train {self.train_id} picked up  Car {car.car_id}")
    
    def drop_off(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Train {self.train_id} dropped off Car {car.car_id} at {car.destination}")
    
    def car_count(self):
        return len(self.cars)

class TrainManager:
    def __init__(self):
        self.trains = []
    
    def add_train(self, train):
        self.trains.append(train)
    
    def get_car_count(self, train_id):
        for train in self.trains:
            if train.train_id == train_id:
                return train.car_count()
        return None
#usage
car1 = Car(1, "Station A", "Station B")
car2 = Car(2, "Station B", "Station C")

trainA = Train("A", 5)
trainB = Train("B", 5)

trainA.pick_up(car1)
trainB.pick_up(car2)
trainB.pick_up(car2)
trainA.pick_up(car1)

trainA.drop_off(car1)
trainA.drop_off(car1)

train_manager = TrainManager()
train_manager.add_train(trainA)
train_manager.add_train(trainB)

print(f"Train A has {train_manager.get_car_count('A')} cars")
print(f"Train B has {train_manager.get_car_count('B')} cars")