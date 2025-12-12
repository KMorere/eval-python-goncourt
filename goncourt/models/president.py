from dataclasses import dataclass
from datetime import date
from .person import Person
from .book import Book
from business.goncourt import Goncourt
from copy import deepcopy
from typing import Optional
import logging

from .selection import Selection


@dataclass
class President(Person):
    """Président décidant des sélections."""
    id: Optional[int] = None

    def set_selection(self):
        """Initialise le déroulement d'une sélection par le président."""
        goncourt: Goncourt = Goncourt()

        # Read database for the selection
        dates = goncourt.set_selection_dates()

        match goncourt.get_selections_by_year(2025):
            case 0:
                goncourt.add_selection_date(dates[0])
                goncourt.add_book_at_date(dates[0], goncourt.get_books())
                # Save on database
                for i in range(len(goncourt.get_books())):
                    goncourt.set_selection(Selection(selection_date=dates[0],
                                                     id_president=1,
                                                     id_book=goncourt.get_books()[i].id))
                logging.info("Sélection 1 initialisé par %s %s.", self.first_name, self.last_name)
            case 1:
                # Save on database
                self.add_selection(dates[1], dates[0], 8, "Sélection 2 initialisé par %s %s.", goncourt)
            case 2:
                # Save on database
                self.add_selection(dates[2], dates[1], 4, "Sélection 3 initialisé par %s %s.", goncourt)
            case 3:
                # Vote randomly
                _date = dates[3]
                goncourt.add_selection_date(_date)
                books = goncourt.start_vote(_date, dates[2])
                for book in books:
                    print(book)
                print("\nGagnant : ", books[0])
                logging.info("Sélection terminé.")

    def add_selection(self, current_date: date, previous_date: date, amount: int, log: str, goncourt: Goncourt):
        """Ajoute une nouvelle date et des livres sur une sélection."""
        goncourt.add_selection_date(current_date)
        self.input_selection(current_date, goncourt.get_selections_by_date(previous_date), amount, goncourt)
        logging.info(log, self.first_name, self.last_name)

    def input_selection(self, _date: date, books: list[Book], amount: int, goncourt: Goncourt):
        """Demande au président les livres à ajouter dans la sélection."""
        current_books: list[Book] = deepcopy(books)
        new_books: list[Book] = []

        while amount > 0:
            read = input(f"Entrez l'id des livres à ajouter (encore {amount} fois) : "
                         f"{list(map(self.get_book_id, current_books))} : ")
            if read.isdigit() and (goncourt.get_book_by_id(int(read)) in current_books):
                current_books.remove(goncourt.get_book_by_id(int(read)))
                new_books.append(goncourt.get_book_by_id(int(read)))
                amount -= 1

        for book in new_books:
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
