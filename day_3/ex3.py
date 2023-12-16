class Appliance:
    def start(self):
        print("Turn On")

class Toaster(Appliance):
    def start(self):
        print("Make toast")


if __name__ == "__main__":
    blender = Appliance()
    blender.start()

    toaster = Toaster()
    toaster.start()

    oven = Appliance()
    oven.start()
    