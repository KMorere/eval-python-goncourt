from dataclasses import dataclass
from datetime import date
from .person import Person
from .book import Book
from business.goncourt import Goncourt
from copy import deepcopy


@dataclass
class President(Person):
    """Président décidant des sélections."""
    def set_selection(self, _date: date):
        goncourt: Goncourt = Goncourt()
        if len(goncourt.selection.keys()) == 0:
            #goncourt.add_selection_date(date(2025, 9, 3))
            goncourt.add_book_at_date(date(2025, 9, 3), goncourt.get_books())

        goncourt.add_selection_date(_date)

    def input_selection(self, _date: date, books: list[Book], amount: int):
        current_books: list[Book] = []
        current_books = deepcopy(books)
        input(f"Entrez l'id des livres à ajouter : [{current_books}]")

    def vote(self, book: Book) -> str:
        from business.goncourt import Goncourt
        Goncourt().do_vote(self, book)
        return f"{self} a voté pour {book.title}."
