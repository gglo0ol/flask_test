import sqlite3


class DataBase:

    def __init__(self, name: str):
        self.con = sqlite3.connect(name)
        self.cursor = self.con.cursor()

    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS data(name, date, status, descriotion)')
        self.con.commit()

    def insert_row(self, data):
        row = (data.name, data.date, data.status, data.description)
        self.cursor.execute("INSERT INTO data VALUES(?, ?, ?, ?)", row)
        self.con.commit()

    def get_all(self, order_by:str = 'date'):
        result = self.cursor.execute(f"SELECT * FROM data ORDER BY {order_by}")
        return result

    def all_delete(self):
        self.cursor.execute("DELETE FROM data")
        self.con.commit()

    def close(self):
        self.con.close()

