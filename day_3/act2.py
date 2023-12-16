class Person:
    def __init__(self,in_name,in_age):
        self.name = in_name
        self.age = in_age
      
    def get_name(self):
        return self.name
  
class Customer(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.ticket = False
        self.zoo = None
  
    def buy_ticket(self):
        self.ticket = True
        if self.age < 18:
            print(f"{self.name} has purchased a child ticket")
        else:
            print(f"{self.name} has purchased an adult ticket")
  
    def enter_zoo(self,zoo):
        self.zoo = zoo
        zoo.add_customer(self.name)
        self.ticket = False
  
    def exit_zoo(self,zoo):
        zoo.remove_customer(self.name)
        self.zoo = None

class Zoo:
    def __init__(self,name="Local Zoo"):
        self.name = name
        self.animals = []
        self.customers = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{self.name} has a(n) {animal}")
  
    def add_animals(self, animals):
        self.animals.extend(animals)
        print(f"{self.name} has many animals")
  
    def add_customer(self, name):
        self.customers.append(name)
        print(f"{name} has entered {self.name}")

    def remove_customer(self, name):
        self.customers.remove(name)
        print(f"{name} has left {self.name}")
  
    def visit_animals(self):
        for a in self.animals:
            print(f"visiting {a.get_name()}")
            a.make_noise()
            a.eat_food()

class Animal:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def make_noise(self):
        print(f"{self.name} says {self.noise}")
    def eat_food(self):
        print(f"{self.name} eats {self.food}")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.noise = "Chirp"
        self.food = "Worms"

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_noise(self):
        print("Blub")
    def eat_food(self):
        print("Algae")

class Chimp(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_noise(self):
        print("Ooh ooh")
    def eat_food(self):
        print("Bananas")

if __name__ == "__main__":

    nycZoo = Zoo("NYC Zoo")

    salmon = Fish("salmon")
    robin = Bird("robin")
    bonobo = Chimp("bonobo")
    nycZoo.add_animals([salmon, robin, bonobo])

    alice = Customer("Alice",25)
    bob = Customer("Bob",20)
    charlie = Customer("Charlie",10)
    dave = Customer("Dave",30)
    for c in [alice, bob, charlie, dave]:
        c.buy_ticket()
        c.enter_zoo(nycZoo)
        nycZoo.visit_animals()
    for c in [alice, bob, charlie, dave]:
        c.exit_zoo(nycZoo)