from models.jury import Jury
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class JuryDao(Dao[Jury]):
    def read(self, id_jury: int) -> Optional[Jury]:
        jury: Optional[Jury]

        with Dao.connection.cursor() as cursor:
            query = """
            SELECT * FROM jury
            LEFT JOIN person ON person.id_person = jury.id_person
            WHERE id_jury = %s
            """
            cursor.execute(query, (id_jury,))
            record = cursor.fetchone()
        if record is not None:
            jury = Jury(record['first_name'], record['last_name'])
            jury.id = record['id_jury']
            jury.password = record['jury_password']
        else:
            jury = None

        return jury

    def read_all(self) -> Optional[list[Jury]]:
        jury: Optional[list[Jury]]

        with Dao.connection.cursor() as cursor:
            query = """
                    SELECT * FROM vote 
                    LEFT JOIN person ON person.id_person = jury.id_person
                    WHERE id_jury = %s
                    """
            cursor.execute(query)
            record = cursor.fetchall()
        if record is not None:
            jury = [Jury(rec['first_name'], rec['last_name']) for rec in record]
            for i in range(cursor.rowcount):
                jury[i].id = record[i]['id_jury']
                jury[i].password = record[i]['jury_password']
        else:
            jury = None

        return jury
