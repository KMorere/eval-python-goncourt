from models.publisher import Publisher
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class PublisherDao(Dao[Publisher]):
    def read(self, id_publisher: int) -> Optional[Publisher]:
        publisher: Optional[Publisher]

        with Dao.connection.cursor() as cursor:
            query = "SELECT * FROM publisher WHERE id_publisher = %s"
            cursor.execute(query, (id_publisher,))
            record = cursor.fetchone()
        if record is not None:
            publisher = Publisher(record['id_publisher'], record['name'])
        else:
            publisher = None

        return publisher

    def read_all(self) -> Optional[list[Publisher]]:
        publisher: Optional[list[Publisher]]

        with Dao.connection.cursor() as cursor:
            query = "SELECT * FROM publisher"
            cursor.execute(query, )
            record = cursor.fetchone()
        if record is not None:
            publisher = [Publisher(rec['id_publisher'], rec['name']) for rec in record]
            #publisher.id = [rec['id_publisher'] for rec in record]
        else:
            publisher = None

        return publisher
