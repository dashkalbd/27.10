from datetime import date


class Book:
    def __init__(self, title="Без назви", year=2000, publisher="Невідомо",
                 genre="Невідомо", author="Невідомо", price=0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        self.title = input("Назва: ")
        self.author = input("Автор: ")
        self.year = int(input("Рік видання (напр. 2015): "))
        self.publisher = input("Видавець: ")
        self.genre = input("Жанр: ")
        self.price = float(input("Ціна, грн: "))

    def display(self):
        print("Назва:", self.title)
        print("Автор:", self.author)
        print("Рік видання:", self.year)
        print("Класика:", self.is_classic())
        print("Видавець:", self.publisher)
        print("Жанр:", self.genre)
        print("Ціна:", self.price, "грн")

    def is_classic(self):
        return date.today().year - self.year >= 50

    def add_price(self, amount=50):
        self.price = self.price + amount

    def same_author(self, other_book):
        return self.author == other_book.author

    def __str__(self):
        return f"«{self.title}», {self.author}, {self.year}, {self.price} грн"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.price < other.price


book1 = Book()
book2 = Book("Кобзар", 1840, "Абабагаламага", "поезія", "Тарас Шевченко", 400)
book3 = Book("Тигролови", 1944, "Фоліо", "пригоди", "Іван Багряний", 250)

print(book1)
print(book2)
print(book3)

print()
book2.add_price()
book3.add_price(100)
print(book2)
print(book3)

print()
print("book2 == book3:", book2 == book3)
print("book3 < book2:", book3 < book2)
print("Той самий автор:", book2.same_author(book3))