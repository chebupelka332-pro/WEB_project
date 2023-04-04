import sqlalchemy
from .db_session import SqlAlchemyBase


class Process(SqlAlchemyBase):
    __tablename__ = 'processes'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    duration = sqlalchemy.Column(sqlalchemy.String, nullable=False)  # Format "01:30" один час тридцать минут
    specialty = sqlalchemy.Column(sqlalchemy.String, nullable=False)  # Специальность мастера который может
    # делать эту работу