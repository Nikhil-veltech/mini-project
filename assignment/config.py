import urllib.parse

class Config:
    password = urllib.parse.quote_plus("Vtu@26790")

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{password}@localhost/todo_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False