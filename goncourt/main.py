from business.goncourt import Goncourt
from datetime import date
from models.book import Book


def initialize_selection(goncourt: Goncourt):
    dates: list[date] = [date(2025, 9, 3),
                         date(2025, 10, 7),
                         date(2025, 10, 28),
                         date(2025, 11, 4)]

    books_id: list[list[int]] = [goncourt.get_books(),
                                 [1, 2, 3, 6, 7, 10, 11, 15],
                                 [1, 2, 3, 7],
                                 [3]]

    for i, _date in enumerate(dates):
        goncourt.add_selection_date(_date)
        for book in books_id[i]:
            if type(book) is int:
                book = goncourt.get_book_by_id(book)
            goncourt.add_book_at_date(_date, book)
            if i == 2:
                goncourt.votes[book] = 0

    print(goncourt.display_selection())


def main() -> None:
    """Programme principal."""
    goncourt: Goncourt = Goncourt()
    initialize_selection(goncourt)

    #print(goncourt.display_books())


if __name__ == "__main__":
    main()
