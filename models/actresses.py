from sqlalchemy import Column, Integer, String
from db.base import Base


class Actresses(Base):
    __tablename__ = 'actresses'

    id = Column(Integer, primary_key=True, doc='Универсальный идентификатор записи', index=True)
    actresses_link = Column(String, doc='Ссылка на актрису')

    def __str__(self):
        return f'{self.id}, {self.actresses_link}'
