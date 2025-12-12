from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import ClassVar, Optional
import pymysql.cursors
from pymysql.cursors import DictCursor


@dataclass
class Dao[T](ABC):
    """CLasse abstraite des classes DAO."""
    connection: ClassVar[pymysql.Connection] = \
        pymysql.connect(host='localhost',
                        user='goncourt',
                        password='evaluation',
                        database='goncourt',
                        cursorclass=DictCursor)

    @abstractmethod
    def read(self, id_entity: int) -> Optional[T]:
        """Renvoit la colomne correspondant à l'id 'id_entity' d'une table."""
        ...

    @abstractmethod
    def read_all(self) -> Optional[list[T]]:
        """Renvoit toute les données associées à une table."""
        ...
