from models.book import Book
from models.author import Author
from models.publisher import Publisher
from models.jury import Jury
from models.selection import Selection
from models.voter import Voter
from datetime import date
from typing import Union
import locale

from daos.book_dao import BookDao
from daos.author_dao import AuthorDao
from daos.publisher_dao import PublisherDao
from daos.selection_dao import SelectionDao


class Goncourt:
    """Couche métier de l'application :
    - winners : collection des gagnants du concour par année
    - selection : collection représentant une sélection de livre par date
    """
    winners: dict[str, Book] = {}
    selection: dict[date, list[Book]] = {}
    votes: dict[Book, int] = {}

#region Méthode de classe
    @classmethod
    def add_selection_date(cls, _date: date):
        cls.selection[_date] = []

    @classmethod
    def add_book_at_date(cls, _date: date, book: Union[Book, list[Book]]):
        if type(book) is list:
            for b in book:
                cls.selection.get(_date).append(b)
        else:
            cls.selection.get(_date).append(book)

    @classmethod
    def display_selection(cls) -> None:
        """Affichage des livres de chaque sélection."""
        dates: list[date] = list(cls.selection.keys())
        locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

        for i, books in enumerate(cls.selection.values()):
            print(f"[Sélection {i+1} du {dates[i].strftime('%A %d %B %Y')}]")
            for book in books:
                print(book)
                print()

    @classmethod
    def display_books(cls):
        """Affichage de tout les livres."""
        for book in cls.get_books():
            print(book)
            print()

    @classmethod
    def get_book_by_year(cls, year: str) -> Book:
        return cls.winners.get(year)

    @classmethod
    def add_vote(cls, book: Book):
        if cls.votes.get(book):
            cls.votes[book] += 1

    @classmethod
    def do_vote(cls, voter: Voter, book: Book) -> str:
        if cls.votes.get(book):
            cls.votes[book] += 1
        return voter.vote(book)
#endregion

#region Méthodes statiques
    @staticmethod
    def get_book_by_id(id_book: int) -> Book:
        return BookDao().read(id_book)

    @staticmethod
    def get_books() -> list[Book]:
        return BookDao().read_all()

    @staticmethod
    def get_author_by_id(id_author: int) -> Author:
        return AuthorDao().read(id_author)

    @staticmethod
    def get_publisher_by_id(id_publisher: int) -> Publisher:
        return PublisherDao().read(id_publisher)

    @staticmethod
    def get_selection_by_id(id_selection: int) -> Selection:
        return SelectionDao().read(id_selection)

    @staticmethod
    def get_selections_by_year(year: int) -> int:
        selection: list[Selection] = SelectionDao().read_all()
        if selection is None:
            return 0
        new_selection: set[Selection] = set()
        for sel in selection:
            if sel.selection_date.year == year:
                new_selection.add(sel)
        return len(new_selection)

    @staticmethod
    def get_selections() -> list[Selection]:
        return SelectionDao().read_all()

    @staticmethod
    def set_selection(selection: Selection) -> int:
        return SelectionDao().create(selection)
#endregion

    @classmethod
    def start_test(cls):
        new_author: Author = Author("Great", "Author")
        new_publisher: Publisher = Publisher("Publisher")
        new_book: Book = Book(0, "Book", "I'm a book !", new_author, new_publisher,
                            date(2025, 1, 1), 0, "", 0, [])

        new_book2: Book = Book(0, "Book the second", "It's book the second, electric boogaloo !",
                                Author("Bad", "Author"), Publisher("Bookworm"),
                                date(2025, 1, 1), 0, "", 0, [])

        cls.add_selection_date(date(2025, 1, 1))
        for book in [new_book, new_book2]:
            cls.add_book_at_date(date(2025, 1, 1), book)

        cls.display_selection()

        new_Jury: Jury = Jury("Unbiased", "Person")
        print(cls.do_vote(new_Jury, new_book))
