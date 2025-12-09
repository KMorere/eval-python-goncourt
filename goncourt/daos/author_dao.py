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
            query = "SELECT * FROM author"
            cursor.execute(query)
            record = cursor.fetchall()
        if record is not None:
            author = [Author(rec['id_author'], rec['id_person']) for rec in record]
            author.id = [rec['id_author'] for rec in record]
        else:
            author = None

        return author
