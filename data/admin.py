import sqlalchemy
from .db_session import SqlAlchemyBase


class Admin(SqlAlchemyBase):
    __tablename__ = 'admins'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    login = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)  # Пока будет не кэшированым а просто хранится здесь
    number = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    info = sqlalchemy.Column(sqlalchemy.String, nullable=False)