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

    def add_user(self, user_id, username, fullname, status):
        with self.connection:
            return self.cursor.execute('INSERT INTO "users" ("user_id", "username", "fullname", "status") '
                                       'VALUES (?, ?, ?, ?)', (user_id, username, fullname, status))


    def user_status(self, user_id):
        with self.connection:
            return self.cursor.execute(f'SELECT "status" FROM "users" WHERE "user_id"=?', (user_id,)).fetchall()[0]
