from typing import Protocol
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .book import Book


class Voter(Protocol):
    def vote(self, book: 'Book'):
        ...
