import sqlite3
import datetime


class DataBase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute(f'SELECT * FROM "users" WHERE user_id="{user_id}"').fetchall()
            return bool(len(result))

    def add_user(self, user_id):
        with self.connection:
            date = datetime.datetime.now()
            self.user_exists(user_id)
            return self.cursor.execute("INSERT INTO 'users' ('user_id', 'date') VALUES (?, ?)", (user_id, date,))

    def add_count(self, user_id, count):
        with self.connection:
            count = self.user_count(user_id) + count
            return self.cursor.execute('UPDATE "users" SET "count" = ? WHERE "user_id" = ?', (count, user_id,))

    def user_count(self, user_id):
        with self.connection:
            result = self.cursor.execute(f'SELECT "count" FROM "users" WHERE user_id="{user_id}"').fetchmany(1)
            return int(result[0][0])

    def user_date(self, user_id):
        with self.connection:
            result = self.cursor.execute(f'SELECT "date" FROM "users" WHERE user_id="{user_id}"').fetchmany(1)
            return result[0][0]

