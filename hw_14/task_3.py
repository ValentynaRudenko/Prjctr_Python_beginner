class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate_5(self):
        self.speed += 5
        print(f"Accelerating to {self.speed} kph")

    def brake_5(self):
        self.speed -= 5
        print(f"Braking to {self.speed} kph")


ford_mustang = Car("Ford", "Mustang", 2022, 200)

ford_mustang.accelerate_5()
ford_mustang.brake_5()
