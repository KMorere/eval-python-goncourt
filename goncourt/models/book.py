from dataclasses import dataclass
from datetime import date
from typing import TYPE_CHECKING, Union, Optional

if TYPE_CHECKING:
    from .author import Author
    from .publisher import Publisher


@dataclass
class Book:
    """Livre présent dans le Goncourt :
    - title : titre du livre
    - summary : résumé
    - author : auteur du livre
    - editor : éditeur du livre
    - characters : personnages principaux
    - published_date : date de publication
    - page_amount : nombre de pages
    - isbn : international standard book number
    - price : prix du livre
    """
    id: Optional[int]
    title: str
    summary: str
    author: 'Author'
    editor: 'Publisher'
    published_date: date
    page_amount: int
    isbn: str
    price: float
    characters: Union[str | list[str]]

    def __str__(self) -> str:
        book = f"Titre : {self.title},\n"
        book += f"\t- par {self.author}\n"
        book += f"\t- édition {self.editor}."
        return book
