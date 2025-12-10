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

    def read(self, id_selection: int) -> Optional[Selection]:
        selection: Optional[Selection]

        with Dao.connection.cursor() as cursor:
            query = """
            SELECT * FROM selection 
            LEFT JOIN book ON book.id_book = selection.id_book
            WHERE id_selection = %s
            """
            cursor.execute(query, (id_selection,))
            record = cursor.fetchone()
        if record is not None:
            selection = Selection(selection_date=record['selection_date'],
                                  id_president=record['id_president'],
                                  id_book=record['id_book'])
            selection.id = record['id_selection']
        else:
            selection = None

        return selection

    def read_all(self) -> Optional[list[Selection]]:
        selection: Optional[list[Selection]]

        with Dao.connection.cursor() as cursor:
            query = """
                    SELECT * FROM selection 
                    LEFT JOIN book ON book.id_book = selection.id_book
                    """
            cursor.execute(query)
            record = cursor.fetchall()
        if record is not None:
            selection = [Selection(rec['selection_date'],
                                   rec['id_president'],
                                   rec['id_book'])
                         for rec in record]
            for i in range(cursor.rowcount):
                selection[i].id = record[i]['id_selection']
        else:
            selection = None

        return selection
