from dataclasses import dataclass
from .person import Person
from .book import Book


@dataclass
class Jury(Person):
    def vote(self, book: Book) -> str:
        return f"{self} voted for {book.title}."
