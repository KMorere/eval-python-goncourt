from abc import ABC
from dataclasses import dataclass


@dataclass
class Person(ABC):
    """Classe abstraitre représentant une personne."""
    first_name: str
    last_name: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
