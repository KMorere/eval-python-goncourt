from business.goncourt import Goncourt


def main() -> None:
    """Programme principal."""
    goncourt: Goncourt = Goncourt()
    goncourt.start()


if __name__ == "__main__":
    main()
