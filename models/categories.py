from sqlalchemy import Column, Integer, String
from db.base import Base


class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, doc='Универсальный идентификатор записи', index=True)
    category_link = Column(String, doc='Ссылка на категорию')

    def __str__(self):
        return f'{self.id}, {self.category_link}'
