from business.goncourt import Goncourt
from datetime import date
import logging
from models.president import President


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
    form = "%(asctime)s: %(message)s"
    logging.basicConfig(format=form, level=logging.INFO, datefmt="%H:%m:%S")

    goncourt: Goncourt = Goncourt()
    #initialize_selection(goncourt)

    #print(goncourt.get_selections_by_year(2025))

    #print(goncourt.start_vote(date(2025, 9, 3)))
    goncourt.get_selections_by_date(date(2025, 10, 7))

    while True:
        read: str = input("Entrez le mode de connection : [0 = Utilisateur, 1 = Admin] \n")

        if read.isdigit() and read == "0":
            print("Mode utilisateur")
            goncourt.set_selection_dates()
            goncourt.display_selection()
        else:
            read = input("Entrez le mot de passe : ")

            if read == "evaluation":
                pres: President = President("Jesus", "Christ")
                print(f"Bienvenu {pres}")
                pres.set_selection()


if __name__ == "__main__":
    main()
