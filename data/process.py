import sqlalchemy
from .db_session import SqlAlchemyBase


class Process(SqlAlchemyBase):
    __tablename__ = 'processes'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    admin_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("admins.id"))
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    duration = sqlalchemy.Column(sqlalchemy.String, nullable=False)  # Format "01:30" один час тридцать минут
    info = sqlalchemy.Column(sqlalchemy.Text, nullable=False)  # Информация об услуге
