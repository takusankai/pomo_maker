# Flask アプリでデータベースを使うための設定
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
        db.session.close()
        print('DB initialized')