from .person import Person
from dataclasses import dataclass, field
from typing import Optional

from .book import Book


@dataclass
class Author(Person):
    """Auteur d'un livre :
    - books : liste des livres écrits par l'auteur"""
    id: Optional[int] = None
    books: list[Book] = field(default_factory=list, init=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
