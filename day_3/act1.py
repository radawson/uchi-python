class Race:
    def __init__(self, name, driver_limit, drivers=[]):
        self.name = name
        self.driver_limit = driver_limit
        self.drivers = drivers

    def add_driver(self, driver):
        if len(self.drivers) < self.driver_limit:
            self.drivers.append(driver)

    def get_average_ranking(self):
        # return average ranking of drivers in drivers list
        total_rankings = 0
        for driver in self.drivers:
            total_rankings += driver.get_ranking()
        return total_rankings / len(self.drivers)


class Driver:
    number_of_drivers = 0

    def __init__(self, name, age, ranking):
        self.name = name
        self.age = age
        self.ranking = ranking
        Driver.number_of_drivers += 1

    # Getters and Setters
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return f"New name is {self.name}."

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
        return f"New age is {self.age}."

    def get_ranking(self):
        return self.ranking

    def set_ranking(self, ranking):
        self.ranking = ranking
        return f"New ranking is {self.ranking}."


if __name__ == "__main__":
    my_course = Race("Seattle 500", 4)
    print(my_course.name, my_course.driver_limit, my_course.drivers)

    my_driver = Driver("Dale Earnhardt", 29, 100)
    print(my_driver.get_ranking())
    print(my_driver.number_of_drivers)

    driver2 = Driver("Lewis Hamilton", 36, 83)
    driver3 = Driver("Eliud Kipchoge", 36, 95)
    driver4 = Driver("Sebastian Vettel", 34, 76)
    driver5 = Driver("Ayrton Senna", 34, 99)

    print(driver5.number_of_drivers)

    driver4 = "a penguin"

    print(driver5.number_of_drivers)
