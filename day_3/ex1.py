class Car:
    def start(self):
        print("Vroom!")

if __name__ == "__main__":
    my_car = Car()
    print(my_car.start())

    print(type(my_car))