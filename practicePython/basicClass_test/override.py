from __future__ import annotations
from operator import attrgetter
from my_decorator import decorator as deco


class Page:
    book_title: str = "Python Practice book"

    def __init__(self, num: int, content: str):
        self.num: int = num
        self.content: str = content

    def output(self) -> str:
        return f"{self.content}"

    @classmethod
    def print_pages(cls, *pages: Page):
        print(cls.book_title)
        page_list = list(pages)

        for page in sorted(page_list, key=attrgetter("num")):
            print(page.output())

class TitlePage(Page):
    @deco.overrides(Page)
    def output(self) -> str:
        title: str = super().output()
        return title.upper()

class Length(float):
    def to_cm(self) -> float:
        return super().__str__() + "cm"

class HTMLPageMixin:
    def to_html(self):
        return f"<html><body>{self.output()}</body></html>"

class WebPage(Page, HTMLPageMixin):
    pass


web_page = WebPage(0, "Web content")
print(web_page.to_html())
print(WebPage.__mro__)

title = TitlePage(0, "Book with title")
print(title.output())
pencil_length = Length(16)
print(pencil_length.to_cm())

second = Page(2, "second")
third = Page(3, "third")
first = Page(1, "first")
forth = Page(4, "forth")
# Page.print_pages(first, third, second, forth)
# first.print_pages(first, third, second, forth)
