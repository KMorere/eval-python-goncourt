from dataclasses import dataclass, field
from typing import Optional
from .person import Person
from .book import Book


@dataclass
class Jury(Person):
    """Juré votant pour un livre."""
    id: Optional[int] = None
    password: str = field(default_factory=str, init=False)

    def vote(self, book: Book) -> str:
        from business.goncourt import Goncourt
        Goncourt().do_vote(self, book)
        return f"{self} a voté pour {book.title}."
