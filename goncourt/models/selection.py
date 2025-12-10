from dataclasses import dataclass, field
from datetime import date
from typing import Optional
from .book import Book


@dataclass
class Selection:
    """Classe représentant une sélection."""
    selection_date: date
    id: Optional[int] = None
    id_president: Optional[int] = field(default_factory=int, init=True)
    id_book: Optional[int] = field(default_factory=int, init=True)
    selections: dict[date, list[Book]] = field(default_factory=dict, init=False)
