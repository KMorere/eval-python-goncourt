from dataclasses import dataclass
from datetime import date
from .person import Person
from .book import Book
from business.goncourt import Goncourt
from copy import deepcopy
from typing import Optional

from .selection import Selection


@dataclass
class President(Person):
    """Président décidant des sélections."""
    id: Optional[int] = None

    def set_selection(self):
        goncourt: Goncourt = Goncourt()
        # if len(goncourt.selection.keys()) == 0:
        #     #goncourt.add_selection_date(date(2025, 9, 3))
        #     goncourt.add_book_at_date(date(2025, 9, 3), goncourt.get_books())

        # Read database for the selection
        dates = goncourt.set_selection()

        match len(goncourt.selection.keys()):
            case 0:
                goncourt.add_selection_date(dates[0])
                goncourt.add_book_at_date(dates[0], goncourt.get_books())
                # Save on database
                for i in range(len(goncourt.get_books())):
                    goncourt.set_selection(Selection(selection_date=dates[0],
                                                     id_president=1,
                                                     id_book=goncourt.get_books()[i].id))
                print("Sélection 1 initialisé.")
            case 1:
                _date = dates[1]
                goncourt.add_selection_date(_date)
                self.input_selection(_date, goncourt.selection.get(dates[0]), 8, goncourt)
                # Save on database
            case 2:
                _date = dates[2]
                goncourt.add_selection_date(_date)
                self.input_selection(_date, goncourt.selection.get(dates[1]), 4, goncourt)
                # Save on database
            case 3:
                # Vote randomly
                print()

    def input_selection(self, _date: date, books: list[Book], amount: int, goncourt: Goncourt):
        current_books: list[Book] = deepcopy(books)
        new_books: list[Book] = []

        while amount > 0:
            read = input(f"Entrez l'id des livres à ajouter (encore {amount} fois) : "
                         f"{list(map(self.get_book_id, current_books))} : ")
            if read.isdigit() and (goncourt.get_book_by_id(int(read)) in current_books):
                current_books.remove(goncourt.get_book_by_id(int(read)))
                new_books.append(goncourt.get_book_by_id(int(read)))
                amount -= 1

        for book in new_books: # TODO: Change id_president to this instance's id.
            goncourt.set_selection(Selection(selection_date=_date,
                                             id_president=1,
                                             id_book=book.id))

    @staticmethod
    def get_book_id(book: Book) -> int:
        return book.id

    def vote(self, book: Book) -> str:
        from business.goncourt import Goncourt
        Goncourt().do_vote(self, book)
        return f"{self} a voté pour {book.title}."
