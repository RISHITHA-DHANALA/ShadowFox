class Avenger:
    def __init__(self, name, age, gender, power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.power = power
        self.weapon = weapon

    def info(self):
        print(self.name, self.age, self.gender, self.power, self.weapon)

    def is_leader(self):
        if self.name == "Captain America":
            print(self.name, "is leader")
        else:
            print(self.name, "is not leader")


a1 = Avenger("Captain America", 35, "Male", "Strength", "Shield")
a2 = Avenger("Iron Man", 40, "Male", "Technology", "Armor")
a3 = Avenger("Hulk", 38, "Male", "Strength", "None")

a1.info()
a2.info()
a3.info()

a1.is_leader()
a2.is_leader()
a3.is_leader()
