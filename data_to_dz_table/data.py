from data_to_dz_table.database import create_db, Session
from data_to_dz_table.user import Users
from data_to_dz_table.getting_data import Parser

p = Parser('https://wargm.ru/','server/66235/votes', 'text_steam.txt')
data_list = p.run()


def _data_list(session):
    data = data_list
    for ind,i in enumerate(data, start=0):
        name = data[ind][0]
        steam_id = data[ind][1]
        date_of_reg = data[ind][2]
        user = Users(name, steam_id, date_of_reg)
        session.add(user)

    session.commit()
    session.close()


def create_database(data_list=True):
    create_db()
    if data_list:
        _data_list(Session())

