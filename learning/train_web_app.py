from flask import Flask, render_template

app = Flask(__name)

# Simulate your Train and Car classes
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

# Create some sample data
car1 = Car(1, "Station A", "Station B")
car2 = Car(2, "Station B", "Station C")

trainA = Train("A", 2)
trainB = Train("B", 1)

@app.route('/')
def home():
    return "Welcome to the Train and Car Management System"

@app.route('/pick_up/<train_id>/<car_id>')
def pick_up(train_id, car_id):
    # Simulate pick-up logic
    for car in [car1, car2]:
        if car.car_id == int(car_id):
            train = trainA if train_id == 'A' else trainB
            train.pick_up(car)
            return f"Car {car_id} has been picked up by Train {train_id}"
    return "Car not found"

@app.route('/drop_off/<train_id>/<car_id>')
def drop_off(train_id, car_id):
    # Simulate drop-off logic
    for car in [car1, car2]:
        if car.car_id == int(car_id):
            train = trainA if train_id == 'A' else trainB
            train.drop_off(car)
            return f"Car {car_id} has been dropped off by Train {train_id}"
    return "Car not found"

@app.route('/car_count/<train_id>')
def car_count(train_id):
    # Simulate car count logic
    train = trainA if train_id == 'A' else trainB
    count = train.car_count()
    return f"Train {train_id} currently has {count} cars"

if __name__ == '__main__':
    app.run(debug=True)
