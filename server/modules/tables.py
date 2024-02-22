from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# SQLAlchemyのインスタンスを作成
db = SQLAlchemy()

# ユーザー情報クラスを作成
class Users(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    created_at = db.Column(db.String(50))
    updated_at = db.Column(db.String(50))

    def get_id(self):
        return str(self.user_id)

# ポモドーロタイマー情報クラスを作成
class PomodoroTimers(db.Model):
    pomo_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    maker_user_id = db.Column(db.Integer)
    work_length = db.Column(db.Integer)
    work_music = db.Column(db.String(50))
    break_length = db.Column(db.Integer)
    break_music = db.Column(db.String(50))

# 作業時間情報クラスを作成
class WorkTimes(db.Model):
    work_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    work_length = db.Column(db.Integer)
    start_time = db.Column(db.String(30))
    end_time = db.Column(db.String(30))
