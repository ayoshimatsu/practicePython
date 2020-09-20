from __future__ import annotations
from operator import attrgetter


class Page:
    book_title: str = "Python Practice book"

    def __init__(self, num: int, content: str):
        self.num: int = num
        self.content: str = content

    def output(self) -> str:
        return f"{self.content}"

    @classmethod
    def print_pages(cls, *pages: Page) -> None:
        print(cls.book_title)
        page_list = list(pages)

        for page in sorted(page_list, key=attrgetter("num")):
            print(page.output())

    @staticmethod
    def temp(*sentences: str):
        word_list = list(sentences)
        for word in word_list:
            print(word)


second = Page(2, "second")
third = Page(3, "third")
first = Page(1, "first")
forth = Page(4, "forth")

Page.print_pages(first, third, second, forth)
Page.temp("aaa", "bbb", "ccc")
