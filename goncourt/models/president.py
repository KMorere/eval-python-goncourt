from dataclasses import dataclass
from datetime import date
from .person import Person
from .book import Book
from business.goncourt import Goncourt
from copy import deepcopy
from typing import Optional


@dataclass
class President(Person):
    """Président décidant des sélections."""
    id: Optional[int] = None

    def set_selection(self, _date: date):
        goncourt: Goncourt = Goncourt()
        # if len(goncourt.selection.keys()) == 0:
        #     #goncourt.add_selection_date(date(2025, 9, 3))
        #     goncourt.add_book_at_date(date(2025, 9, 3), goncourt.get_books())

        # Read database for the selection
        #goncourt.get_selections()

        match len(goncourt.selection.keys()):
            case 0:
                goncourt.add_book_at_date(date(2025, 9, 3), goncourt.get_books())
                # Save on database
            case 1:
                _date = date(2025, 10, 7)
                self.input_selection(_date, goncourt.selection.get(_date), 8, goncourt)
                # Save on database
            case 2:
                _date = date(2025, 10, 28)
                self.input_selection(_date, goncourt.selection.get(_date), 4, goncourt)
                # Save on database
            case 3:
                # Vote randomly
                print()

        goncourt.add_selection_date(_date)

    def input_selection(self, _date: date, books: list[Book], amount: int, goncourt: Goncourt):
        current_books: list[Book] = []
        new_books: list[Book] = []
        current_books = deepcopy(books)

        for i in range(amount):
            read = input(f"Entrez l'id des livres à ajouter (encore {amount-i} fois) : "
                         f"{list(map(self.get_book_id, current_books))} : ")
            if read.isdigit() and (goncourt.get_book_by_id(int(read)) in current_books):
                current_books.remove(goncourt.get_book_by_id(int(read)))
                new_books.append(goncourt.get_book_by_id(int(read)))

        print(new_books)

    @staticmethod
    def get_book_id(book: Book) -> int:
        return book.id

    def vote(self, book: Book) -> str:
        from business.goncourt import Goncourt
        Goncourt().do_vote(self, book)
        return f"{self} a voté pour {book.title}."
