from dataclasses import dataclass
from datetime import date
from typing import TYPE_CHECKING, Union, Optional

if TYPE_CHECKING:
    from .author import Author
    from .publisher import Publisher


@dataclass
class Book:
    title: str
    summary: str
    author: Optional['Author']
    editor: Optional['Publisher']
    characters: Union[str | list[str]]
    published_date: date
    page_amount: int
    isbn: str
    price: float

    def __str__(self) -> str:
        return f"Title : {self.title}, written by {self.author} and edited by {self.editor}."
