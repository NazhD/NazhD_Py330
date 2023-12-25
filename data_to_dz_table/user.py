
from data_to_dz_table.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    steam_id = Column(String(250))
    date_of_registration = Column(String(250))

    def __init__(self, name,steam_id,date_of_registration):
        self.name = name
        self.steam_id = steam_id
        self.date_of_registration = date_of_registration

    def __repr__(self):
        return f"Пользователь (Никнейм: {self.name} Стим id: {self.steam_id} Дата регистрации: {self.date_of_registration})"




