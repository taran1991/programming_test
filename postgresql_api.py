
import psycopg2
import scraping

HOST = "localhost"
DB = "news"
USER = "postgres"
PASSWORD = 'postgres'


class PostgreSQL(object):
    def __init__(self, host=HOST, db=DB, user=USER, password=PASSWORD):
        self.host=host,
        self.database=db,
        self.user=user,
        self.password=password

    def connect_to_db(self, host=HOST, db=DB, user=USER, password=PASSWORD):
        conn = psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=password)
        return conn

    def create_table(self):
        """ create tables in the PostgreSQL database"""
        command = (
            """
            DROP TABLE  IF EXISTS news;
            CREATE TABLE news (
                id SERIAL PRIMARY KEY,
                url VARCHAR(255) NOT NULL,
                title VARCHAR(255) NOT NULL,
                short_description VARCHAR(5000),
                publish_date timestamp
            )
            """)
        conn = None
        try:
            conn = self.connect_to_db()
            cur = conn.cursor()
            cur.execute(command)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def save_news_to_db(self, news):
        sql = "INSERT INTO news(url, title, short_description, publish_date) VALUES(%s, %s, %s, %s)"
        conn = None
        try:
            conn = self.connect_to_db()
            cur = conn.cursor()
            cur.executemany(sql, news)
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


if __name__ == '__main__':
    db = PostgreSQL()
    db.create_table()
    news = scraping.scrap_news()
    db.save_news_to_db(news)

