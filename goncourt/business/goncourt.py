from models.book import Book
from models.author import Author
from models.publisher import Publisher
from models.jury import Jury
from models.voter import Voter
from datetime import date


class Goncourt:
    @staticmethod
    def do_vote(voter: Voter, book: Book) -> str:
        return voter.vote(book)

    @staticmethod
    def start():
        new_author: Author = Author("Great", "Author")
        new_publisher: Publisher = Publisher("Publisher")
        new_book: Book = Book("Book", "I'm a book !", new_author, new_publisher, [],
                              date(2025, 1, 1), 0, "", 0)

        print(new_book)

        new_Jury: Jury = Jury("Unbiased", "Person")
        print(Goncourt.do_vote(new_Jury, new_book))
