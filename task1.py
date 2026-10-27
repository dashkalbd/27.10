from datetime import date


class Car:
    def __init__(self, model="Невідомо", year=2000, manufacturer="Невідомо",
                 engine_volume=1.0, color="білий", price=0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Модель: ")
        self.manufacturer = input("Виробник: ")
        self.year = int(input("Рік випуску (напр. 2018): "))
        self.engine_volume = float(input("Об'єм двигуна, л (напр. 1.6): "))
        self.color = input("Колір: ")
        self.price = float(input("Ціна, $: "))

    def display(self):
        print("Модель:", self.model)
        print("Виробник:", self.manufacturer)
        print("Рік випуску:", self.year)
        print("Вік авто:", self.get_age())
        print("Об'єм двигуна:", self.engine_volume, "л")
        print("Колір:", self.color)
        print("Ціна: $", self.price)

    def get_age(self):
        return date.today().year - self.year

    def change_price(self, new_price=None, percent=None):
        if new_price is not None:
            self.price = new_price
        elif percent is not None:
            self.price = self.price * (100 - percent) / 100

    def repaint(self, new_color="білий"):
        self.color = new_color

    def __str__(self):
        return f"{self.manufacturer} {self.model}, {self.year}, {self.color}, {self.price} $"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price


car1 = Car()
car2 = Car("Corolla", 2020, "Toyota", 1.6, "сірий", 18000)
car3 = Car("Golf", 2019, "VW", 1.4, "чорний", 16000)

print(car1)
print(car2)
print(car3)

print()
car2.change_price(new_price=17000)
car3.change_price(percent=10)
car3.repaint()
car1.repaint("червоний")
print(car1)
print(car2)
print(car3)

print()
print("car2 == car3:", car2 == car3)
print("car3 < car2:", car3 < car2)