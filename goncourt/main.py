from business.goncourt import Goncourt


def main() -> None:
    """Programme principal."""
    goncourt: Goncourt = Goncourt()

    print(goncourt.get_book_by_id(1))
    print()

    print(goncourt.display_books())


if __name__ == "__main__":
    main()
