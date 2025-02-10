import datetime as _dt
import sqlalchemy as _sqlalchemy
import database as _database

class Contact(_database.Base):
    __tablename__ = "contacts"
    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True, index = True)
    first_name = _sqlalchemy.Column(_sqlalchemy.String, index = True)
    last_name = _sqlalchemy.Column(_sqlalchemy.String, index = True)
    email = _sqlalchemy.Column(_sqlalchemy.String, index = True, unique=True)
    phone_number = _sqlalchemy.Column(_sqlalchemy.String, index = True)
    date_created = _sqlalchemy.Column(_sqlalchemy.DateTime, default=_dt.datetime.now)