import datetime
import sqlalchemy
from data.db_session import SqlAlchemyBase

from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin

from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = "users"

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String,
                                 unique=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              unique=True)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    hashed_password = sqlalchemy.Column(sqlalchemy.Integer)
    register_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now())

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
