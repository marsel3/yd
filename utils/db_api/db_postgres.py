
import psycopg2
from psycopg2 import Error


class DataBase:
    def __init__(self):
        self.connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="1234",
                                  host="localhost",     # 127.0.0.1/localhost
                                  port="5432",   # 5434/2
                                  database="sport")
        self.cursor = self.connection.cursor()


    def team_games(self):
        with self.connection:
            self.cursor.execute('''SELECT * FROM "CreateDatabase_vidsporta" WHERE "vidsporta_type"=TRUE''')
            return [i[0] for i in self.cursor.fetchall()]


    def solo_games(self):
        with self.connection:
            self.cursor.execute('''SELECT * FROM "CreateDatabase_vidsporta" WHERE "vidsporta_type"=FALSE''')
            return [i[0] for i in self.cursor.fetchall()]


    def treners(self):
        with self.connection:
            self.cursor.execute('''SELECT * FROM "CreateDatabase_trener"''')
            return self.cursor.fetchall()





    def user_exists(self, user_id):
        with self.connection:
            self.cursor.execute(f'''SELECT * FROM "CreateDatabase_users" WHERE user_id='{user_id}' ''')
            return bool(len(self.cursor.fetchall()))

    def add_user(self, user_id, username, fullname, status='user'):
        with self.connection:
            return self.cursor.execute('INSERT INTO "CreateDatabase_users" '
                                       '("user_id", "user_name", "user_fullname", "user_status") '
                                       'VALUES (%s, %s, %s, %s)', (user_id, username, fullname, status))

    def user_status(self, user_id):
        with self.connection:
            self.cursor.execute(f'''SELECT "user_status" FROM "CreateDatabase_users" WHERE "user_id"='{user_id}' ''')
            return self.cursor.fetchall()[0][0]

    def set_status(self, user_id, status):
        with self.connection:
            self.cursor.execute(f'''UPDATE "CreateDatabase_users" 
                                    SET "user_status"='{status}' 
                                    WHERE "user_id"='{user_id}' ''')

    def trener_by_passport(self, passport):
        with self.connection:
            self.cursor.execute(f'''SELECT * FROM "CreateDatabase_trener" WHERE "trener_passport"='{passport}' ''')
            return bool(len(self.cursor.fetchall()))

    def trener_by_tg(self, tg):
        with self.connection:
            self.cursor.execute(f'''SELECT * FROM "CreateDatabase_trener" WHERE "trener_tg"='{tg}' ''')
            return bool(len(self.cursor.fetchall()))


    def trener_info(self, tg):
        with self.connection:
            self.cursor.execute(f'''SELECT * FROM "CreateDatabase_trener" WHERE "trener_tg"='{tg}' ''')
            return self.cursor.fetchall()[0]

    def trener_info_by_id(self, trener_id):
        with self.connection:
            self.cursor.execute(f'''SELECT * FROM "CreateDatabase_trener" WHERE "trener_id"='{trener_id}' ''')
            return self.cursor.fetchall()[0]


    def team_by_trener(self, trener_id):
        with self.connection:
            self.cursor.execute(f'''SELECT * FROM "CreateDatabase_team" WHERE "team_trener_id"='{trener_id}' ''')
            return bool(len(self.cursor.fetchall()))

    def teaminfo_by_id(self, team_id):
        with self.connection:
            self.cursor.execute(f'''SELECT * FROM "CreateDatabase_team" WHERE "team_id"='{team_id}' ''')
            return self.cursor.fetchall()[0]


    def teaminfo_by_trener(self, trener_id):
        with self.connection:
            self.cursor.execute(f'''SELECT * FROM "CreateDatabase_team" WHERE "team_trener_id"='{trener_id}' ''')
            return self.cursor.fetchall()[0]


    def teams_by_vidsporta(self, vidsporta):
        with self.connection:
            self.cursor.execute(f'''SELECT "team_id", "team_name" FROM "CreateDatabase_team" WHERE "team_vidsporta_id"='{vidsporta}' ''')
            return self.cursor.fetchall()


    def search_by_team(self, team):
        with self.connection:
            self.cursor.execute(f'''SELECT "team_id", "team_name" FROM "CreateDatabase_team" WHERE "team_name"
                                    like '%{team}%' ''')
            return self.cursor.fetchall()

    def vidsporta(self, type):
        with self.connection:
            self.cursor.execute(f'''SELECT "vidsporta_id", "vidsporta_name" FROM "CreateDatabase_vidsporta" WHERE "vidsporta_type"='{type}' ''')
            return self.cursor.fetchall()

    def vidsporta_type(self, id):
        with self.connection:
            self.cursor.execute(f'''SELECT "vidsporta_type" FROM "CreateDatabase_vidsporta" WHERE "vidsporta_id"='{id}' ''')
            return self.cursor.fetchall()[0][0]

    def vidsporta_type_by_team(self, id):
        with self.connection:
            self.cursor.execute(f'''SELECT "vidsporta_type" FROM "CreateDatabase_vidsporta" WHERE "vidsporta_id"=
                                (SELECT "team_vidsporta_id" FROM "CreateDatabase_team" WHERE "team_id"='{id}') ''')
            return self.cursor.fetchall()[0][0]


    def results_solo_byteam(self, team_id):
        with self.connection:
            self.cursor.execute(f'''SELECT g."games_name", rs."game_result"
                                    FROM "CreateDatabase_resultssolo" AS rs
                                    JOIN "CreateDatabase_games" AS g ON rs."resultsolo_id_id" = g."games_id"
                                    WHERE rs."resultsolo_solo_id" = '{team_id}'
                                ''')
            return self.cursor.fetchall()


    def results_team_byteam(self, team_id):
        with self.connection:
            self.cursor.execute(f'''

                                ''')
            return self.cursor.fetchall()


    def final_results_byteam(self, team_id):
        with self.connection:
            self.cursor.execute(f'''
                                    SELECT * FROM "CreateDatabase_competition" WHERE "competition_team_id" = '{team_id}' 
                                ''')
            return self.cursor.fetchall()

    def sporstmen_by_team(self, team_id):
        with self.connection:
            self.cursor.execute(f'''
                                    SELECT * FROM "CreateDatabase_sportsmen" WHERE "sportsmen_team_id" = '{team_id}' 
                                ''')
            return self.cursor.fetchall()

db = DataBase()
print(db.final_results_byteam(18))
