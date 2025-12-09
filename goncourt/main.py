from business.goncourt import Goncourt


def main() -> None:
    """Programme principal."""
    goncourt: Goncourt = Goncourt()
    #goncourt.start()

    print(goncourt.get_book_by_id(1))


if __name__ == "__main__":
    main()
