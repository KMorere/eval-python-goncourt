from models.book import Book
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional


@dataclass
class BookDao(Dao[Book]):
    def read(self, id_book: int) -> Optional[Book]:
        book: Optional[Book]

        with Dao.connection.cursor() as cursor:
            query = "SELECT * FROM book WHERE id_book = %s"
            cursor.execute(query, (id_book,))
            record = cursor.fetchone()
        if record is not None:
            book = Book(record['id_book'], record['title'], record['summary'],
                        record['id_author'], record['id_publisher'], record['published_date'],
                        record['page_amount'], record['isbn'], record['price'], record['characters'])
            book.id = record['id_book']
            from business.goncourt import Goncourt
            book.author = Goncourt().get_author_by_id(record['id_author'])
            book.editor = Goncourt().get_publisher_by_id(record['id_publisher'])
        else:
            book = None

        return book

    def read_all(self) -> Optional[list[Book]]:
        book: Optional[list[Book]]

        with Dao.connection.cursor() as cursor:
            query = "SELECT * FROM book"
            cursor.execute(query)
            record = cursor.fetchall()
        if record is not None:
            book = [Book(rec['id_book'], rec['title'], rec['summary'],
                        rec['id_author'], rec['id_publisher'], rec['published_date'],
                        rec['page_amount'], rec['isbn'], rec['price'], rec['characters'])
                    for rec in record]
            for i in range(cursor.rowcount):
                book[i].id = record[i]['id_book']
                from business.goncourt import Goncourt
                book[i].author = Goncourt().get_author_by_id(record[i]['id_author'])
                book[i].editor = Goncourt().get_publisher_by_id(record[i]['id_publisher'])
        else:
            book = None

        return book
