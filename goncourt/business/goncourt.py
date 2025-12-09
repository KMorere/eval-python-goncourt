from models.book import Book
from models.author import Author
from models.publisher import Publisher
from models.jury import Jury
from models.voter import Voter
from datetime import date

from daos.book_dao import BookDao
from daos.author_dao import AuthorDao
from daos.publisher_dao import PublisherDao


class Goncourt:
    """Couche métier de l'application :
    - winners : collection des gagnants du concour par année
    - selection : collection représentant une sélection de livre par date
    """
    winners: dict[str, Book]
    selection: dict[date, list[Book]] = {}

    @classmethod
    def add_selection_date(cls, _date: date):
        cls.selection[_date] = []

    @classmethod
    def add_book_at_date(cls, _date: date, book: Book):
        cls.selection.get(_date).append(book)

    @classmethod
    def display_selection(cls) -> None:
        """Affichage des livres de chaque sélection"""
        for books in cls.selection.values():
            for book in books:
                print(book)
                print()

    @classmethod
    def display_books(cls):
        for book in cls.get_books():
            print(book)
            print()

    @classmethod
    def get_book_by_year(cls, year: str) -> Book:
        return cls.winners.get(year)

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
    def do_vote(voter: Voter, book: Book) -> str:
        return voter.vote(book)

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
