from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


db: SQLAlchemy = SQLAlchemy()


# SQLALchemy class
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)


# To get a user id
def get_user(username):
    return User.query.filter_by(username=username).first()


# To implement user login authentication
class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data):
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(username):
        user_db = get_user(username)
        user_data = UserData(
            username=user_db.username,
            password=user_db.password,
        )

        return UserModel(user_data)
