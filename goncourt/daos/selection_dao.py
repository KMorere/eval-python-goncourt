from pymysql.cursors import DictCursor
from typing import Any, cast, Dict

from models.selection import Selection
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class SelectionDao(Dao[Selection]):
    def create(self, selection: Selection) -> int:
        """Permet l'insertion des données d'une sélection."""
        id_selection: int = 0

        with Dao.connection.cursor() as cursor:
            query = """
            INSERT INTO selection (id_selection, selection_date, id_president, id_book) VALUES
            (%s, %s, %s, %s)
            """
            data = [selection.id, selection.selection_date, selection.id_president, selection.id_book]
            cursor.execute(query, data)
            cursor.connection.commit()
            id_selection = cursor.rowcount

        return id_selection

    @staticmethod
    def selection_from_db(record: Optional[Dict[str, Any]]) -> Selection:
        selection: Selection = Selection(selection_date=record['selection_date'],
                                         id_president=record['id_president'],
                                         id_book=record['id_book'])
        selection.id = record['id_selection']

        return selection

    def read(self, id_selection: int) -> Optional[Selection]:
        selection: Optional[Selection]

        with Dao.connection.cursor(DictCursor) as cursor:
            query = """
            SELECT * FROM selection 
            LEFT JOIN book ON book.id_book = selection.id_book
            WHERE id_selection = %s
            """
            cursor.execute(query, (id_selection,))
            record = cast(Optional[Dict[str, Any]], cursor.fetchone())
        if record is not None:
            selection = self.selection_from_db(record)
        else:
            selection = None

        return selection

    def read_all(self) -> list[Selection]:
        selection: list[Selection] = []

        with Dao.connection.cursor() as cursor:
            query = """
                    SELECT * FROM selection 
                    LEFT JOIN book ON book.id_book = selection.id_book
                    """
            cursor.execute(query)
            record = cursor.fetchall()
        for rec in record:
            selection.append(self.selection_from_db(
                cast(Optional[Dict[str, Any]], cast(object, rec))))

        return selection
