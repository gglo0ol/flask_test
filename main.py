from Random_data import Random_data
from SQLite import DataBase


for i in range(1):
    r = Random_data()
    db = DataBase('service_status')
    db.insert_row(r)
    for item in db.get_all():
        print(item)

    db.close()
