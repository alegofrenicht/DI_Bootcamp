db_info = {'host': 'dpg-ch7a9ojhp8u9bo624se0-a.oregon-postgres.render.com',
           'database': 'mybookstore',
           'psw': 'cNFZAPPjGSBun9WhvMivpdua0WeVgK9l',
           'user': 'mybookstore_user',
           'port': ''}


class Config:
    SECRET_KEY = "qwertyuiop"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"

