from dataclasses import dataclass
from .person import Person
from .book import Book


@dataclass
class Jury(Person):
    """Juré votant pour un livre."""
    def vote(self, book: Book) -> str:
        return f"{self} a voté pour {book.title}."
