import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Master(SqlAlchemyBase):
    __tablename__ = 'masters'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    admin_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("admins.id"))
    start_work_time = sqlalchemy.Column(sqlalchemy.String, nullable=False)  # Format "09:00-21:00"
    end_work_time = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    work_days = sqlalchemy.Column(sqlalchemy.String, nullable=False)  # Format "1,2,3,4,5,6,7" рабочие дни
    # сотрудника через запятую
    admin = orm.relationship('Admin')
