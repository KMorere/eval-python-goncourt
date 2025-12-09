from .person import Person
from dataclasses import dataclass, field

from .book import Book


@dataclass
class Author(Person):
    books: list[Book] = field(default_factory=list, init=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
