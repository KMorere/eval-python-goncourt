from dataclasses import dataclass
from datetime import date
from typing import TYPE_CHECKING, Union

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
    title: str
    summary: str
    author: 'Author'
    editor: 'Publisher'
    characters: Union[str | list[str]]
    published_date: date
    page_amount: int
    isbn: str
    price: float

    def __str__(self) -> str:
        book = f"Title : {self.title},\n"
        book += f"écrit par {self.author}\n"
        book += f"édition {self.editor}."
        return book
