class Page:
    def __init__(self, num: int, content: str):
        self.num = num
        self.content = content

    def output(self):
        return f'{self.content}'

title_page = Page(0, "Book")

class Book:
    def __init__(self, raw_price: int):
        if raw_price < 0:
            raise ValueError("price must be positive")
        self._raw_price: int = raw_price
        self._discount: int = 0

    @property
    def discount(self) -> int:
        return self._discount

    @discount.setter
    def discount(self, value: int):
        if value < 0 or 100 < value:
            raise ValueError("discount must be between 0 and 100")
        self._discount = value

    @property
    def price(self) -> int:
        multi = 100 - self._discount
        return int(self.raw_price * multi / 100)

book = Book(2000)
book._raw_price = 1000

print(book._raw_price)
print(book._discount)

book.discount = 20