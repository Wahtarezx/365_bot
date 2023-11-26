from sqlalchemy import Column, Integer, String, ForeignKey
from db.base import Base
from sqlalchemy.orm import relationship


class Favourite(Base):
    __tablename__ = 'favourite'

    id = Column(Integer, primary_key=True, doc='Универсальный идентификатор записи', index=True)
    video_link = Column(String, doc='Ссылка на видео')
    user_id = Column(Integer, ForeignKey("users.id"), doc='ID пользователя из таблицы users')
    user = relationship('Users', backref='favourite', doc='Объект из таблицы users')

    def __str__(self):
        return f'{self.id}, {self.video_link}'
