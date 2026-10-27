from datetime import date


class Stadium:
    def __init__(self, name="Без назви", opening_date=None, country="Невідомо",
                 city="Невідомо", capacity=0):
        self.name = name
        if opening_date is None:
            self.opening_date = date.today()
        else:
            self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Назва стадіону: ")
        self.country = input("Країна: ")
        self.city = input("Місто: ")
        self.capacity = int(input("Місткість (кількість місць): "))
        day = int(input("День відкриття (1-31): "))
        month = int(input("Місяць відкриття (1-12): "))
        year = int(input("Рік відкриття (напр. 1923): "))
        self.opening_date = date(year, month, day)

    def display(self):
        print("Стадіон:", self.name)
        print("Місто:", self.city)
        print("Країна:", self.country)
        print("Дата відкриття:", self.opening_date.strftime("%d.%m.%Y"))
        print("Працює років:", self.years_open())
        print("Місткість:", self.capacity)
        print("Великий стадіон:", self.is_big())

    def years_open(self):
        return date.today().year - self.opening_date.year

    def is_big(self):
        return self.capacity >= 50000

    def add_seats(self, seats=1000):
        self.capacity = self.capacity + seats

    def fill_percent(self, spectators):
        return spectators / self.capacity * 100

    def __str__(self):
        return (f"{self.name}, {self.city}, {self.country}, "
                f"відкрито {self.opening_date.strftime('%d.%m.%Y')}, місць: {self.capacity}")

    def __eq__(self, other):
        return self.capacity == other.capacity

    def __lt__(self, other):
        return self.capacity < other.capacity


stadium1 = Stadium()
stadium2 = Stadium("Олімпійський", date(1923, 8, 12), "Україна", "Київ", 70050)
stadium3 = Stadium("Арена Львів", date(2011, 10, 29), "Україна", "Львів", 34915)

print(stadium1)
print(stadium2)
print(stadium3)

print()
stadium3.add_seats()
print(stadium3)
stadium3.add_seats(5000)
print(stadium3)

print()
print("stadium2 == stadium3:", stadium2 == stadium3)
print("stadium3 < stadium2:", stadium3 < stadium2)