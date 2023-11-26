from sqlalchemy import Column, Integer, String, Boolean
from db.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, doc='Уникальный идентификатор записи', index=True)
    user_id = Column(Integer, doc='ID пользователя')
    name = Column(String, doc='Имя пользователя', nullable=True)
    user_name = Column(String, doc='Имя пользователя в телеграм', nullable=True)
    subscription = Column(Boolean, doc='Подписка на оповещения от бота', default=False)

    def __str__(self):
        return f'{self.user_name}, {self.id}'
