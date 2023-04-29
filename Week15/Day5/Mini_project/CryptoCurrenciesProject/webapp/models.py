from webapp import db

user_crypto_currency = db.Table('user_crypto_currency',
                                db.Column('user_id', db.Integer, db.ForeignKey('app_user.id'), primary_key=True),
                                db.Column('crypto_currency_id', db.Integer, db.ForeignKey('crypto_currency.id'),
                                          primary_key=True)
                                )


class AppUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    cryptocurrencies = db.relationship('CryptoCurrency', secondary=user_crypto_currency, lazy='subquery',
                                       backref=db.backref('app_users', lazy=True))


class CryptoCurrency(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(64))
    symbol = db.Column(db.String(64))
    slug = db.Column(db.String(64))
    first_historical_data = db.Column(db.String(64))
    last_historical_data = db.Column(db.String(64))
