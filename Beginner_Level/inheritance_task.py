class MobilePhone:
    def __init__(self, screen, network, dualsim, camera, ram, storage):
        self.screen = screen
        self.network = network
        self.dualsim = dualsim
        self.camera = camera
        self.ram = ram
        self.storage = storage

    def call(self):
        print("Calling")

    def receive(self):
        print("Receiving call")


class Apple(MobilePhone):
    def __init__(self, name):
        super().__init__("Touch", "5G", True, "12MP", "4GB", "128GB")
        self.name = name


class Samsung(MobilePhone):
    def __init__(self, name):
        super().__init__("Touch", "5G", True, "16MP", "6GB", "256GB")
        self.name = name


a = Apple("iPhone")
s = Samsung("Galaxy")

a.call()
s.receive()
