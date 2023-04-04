import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Record(SqlAlchemyBase):
    __tablename__ = 'records'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    admin_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("admins.id"))
    process_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("processes.id"))
    start_time = sqlalchemy.Column(sqlalchemy.String, nullable=False)  # Format "09:00"
    admin = orm.relationship('Admin')