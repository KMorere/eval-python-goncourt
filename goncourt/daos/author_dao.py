from models.author import Author
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class AuthorDao(Dao[Author]):
    def read(self, id_author: int) -> Optional[Author]:
        author: Optional[Author]

        with Dao.connection.cursor() as cursor:
            query = "SELECT * FROM author LEFT JOIN person ON person.id_person = author.id_person WHERE id_author = %s"
            cursor.execute(query, (id_author,))
            record = cursor.fetchone()
        if record is not None:
            author = Author(record['first_name'], record['last_name'])
            author.id = record['id_author']
        else:
            author = None

        return author

    def read_all(self) -> Optional[list[Author]]:
        author: Optional[list[Author]]

        with Dao.connection.cursor() as cursor:
            query = "SELECT * FROM author LEFT JOIN person ON person.id_person = author.id_person"
            cursor.execute(query)
            record = cursor.fetchall()
        if record is not None:
            author = [Author(rec['first_name'], rec['last_name']) for rec in record]
            for i in range(cursor.rowcount):
                author[i].id = record[i]['id_author']
        else:
            author = None

        return author
