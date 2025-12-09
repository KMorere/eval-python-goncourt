from typing import Protocol
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .book import Book


class Voter(Protocol):
    """Interface permettant le vote d'un livre."""
    def vote(self, book: 'Book'):
        ...
