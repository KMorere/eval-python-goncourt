from dataclasses import dataclass, field

from .book import Book


@dataclass
class Publisher:
    name: str
    books: list[Book] = field(default_factory=list, init=False)

    def add_book(self, book: Book):
        self.books.append(book)

    def __str__(self) -> str:
        return f"{self.name}"
